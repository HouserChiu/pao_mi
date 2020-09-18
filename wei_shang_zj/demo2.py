import os
import re
from mongo_info import mongo_info_wszj
import requests
from lxml import etree
import urllib3

def get_headers():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'cw1_mobile=pc',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    return headers

def one_page():
    url = 'https://www.229289.com/'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=get_headers(), verify=False)
    res.encoding = "UTF-8"
    html = etree.HTML(res.text)
    temp = html.xpath("//div[@class='wshy']/div")
    url_list = []
    for eve in temp:
        url_list.append(''.join(eve.xpath("./div[@class='hyfl']/h3/a/@href")))
    # print(url_list)
    return url_list
# one_page()

def two_page():
    url_list = one_page()
    url_eve_lists = []
    for url in url_list:
        # 获取大类一级详情页页数，包含所有
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = requests.get(url, headers=get_headers(), verify=False)
        res.encoding = "UTF-8"
        html = etree.HTML(res.text)
        temp1 = ''.join(html.xpath("//div[@class='pages']/cite/text()")).strip()
        temp = re.search('共.*?\/(\d+)页',temp1,re.S).group(1)
        temp_url_list = []
        for i in range(1, int(temp) + 1):
            temp_url_list.append(url + str(i))
        url_eve_lists.append(temp_url_list)
    return url_eve_lists
# two_page()

# 对每一个详情页请求
def three_page():
    url_lists = two_page()
    url_eve_lists = []
    for url_list in url_lists:
        for url in url_list:
            # 获取第一页详情数据
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res = requests.get(url, headers=get_headers(), verify=False)
            res.encoding = "UTF-8"
            html = etree.HTML(res.text)
            temp = html.xpath("//div[@class='extension_ul']/ul/li")
            url_eve_list = []
            for eve in temp:
                url_eve_list.append(''.join(eve.xpath("./a/@href")))
            url_eve_lists.append(url_eve_list)
    return url_eve_lists

def four_page():
    try:
        url_lists = three_page()
        for url_list in url_lists:
            for url in url_list:
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                res = requests.get(url, headers=get_headers(), verify=False)
                res.encoding = "UTF-8"
                html = etree.HTML(res.text)
                user_info = {}
                user_info['nickname'] = ''.join(html.xpath("//div[@class='contact_body']/ul/li[1]/a/text()"))
                try:
                    user_info['wx'] = re.search('<div.*?contact_body.*?微信号</span>(.*?)</li>', res.text, re.S).group(1)
                except AttributeError:
                    user_info['wx'] = ''
                try:
                    user_info['phone_number'] = re.search('<div.*?contact_body.*?手机</span>(.*?)</li>', res.text,
                                                          re.S).group(1)
                except AttributeError:
                    user_info['phone_number'] = ''
                try:
                    user_info['district'] = re.search('<div.*?contact_body.*?地区</span>(.*?)</li>', res.text, re.S).group(1)
                except AttributeError:
                    user_info['district'] = ''
                try:
                    user_info['headimage'] = re.search('<div.*?list-thumb.*?src=(.*?)alt.*?</a>', res.text, re.S).group(
                        1).replace('"', '').replace(' ', '')
                except AttributeError:
                    user_info['headimage'] = ''
                user_info['third_id'] = 'wszj_' + re.search('weishang\/(\d+)\/(\d+)\.html', url).group(2)
                user_info['tag'] = ''.join(html.xpath("//h1[@class='title_trade']/text()"))
                result = ''.join(html.xpath("//div[@class='contact_body']/ul/li[3]/text()"))
                if '女' in result:
                    user_info['gender'] = '2'
                else:
                    user_info['gender'] = '1'
                # if os.path.isfile('%s' % user_info['third_id'] + '.jpg'):
                #     pass
                # else:
                #     with open('%s' % user_info['third_id'] + '.jpg', 'wb') as f:
                #         urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                #         img = requests.get(user_info['headimage'], verify=False).content
                #         f.write(img)
                print(user_info)
                mongo_info_wszj.insert_item(user_info)
    except TimeoutError:
        pass

four_page()
