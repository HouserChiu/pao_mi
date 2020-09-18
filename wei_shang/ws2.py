import os
from mongo_info import mongo_info_wx
import requests
from lxml import etree


def get_headers():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'Hm_lvt_86ef62619c5f1847c0bd95c2cf7b76a7=1590487783; Hm_lpvt_86ef62619c5f1847c0bd95c2cf7b76a7=1590492064',
        'Host': 'www.lyjlgs.com',
        'Referer': 'http://www.lyjlgs.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    return headers


def one_page():
    url_list = []
    url = 'http://www.lyjlgs.com/'
    html = requests.get(url, headers=get_headers()).text
    temp = etree.HTML(html).xpath("//ul[@class='clearfix']/li")
    for eve in temp:
        eves = eve.xpath("./a/@href")
        url_temp = ''.join(eves)
        url_eve = 'http://www.lyjlgs.com' + url_temp
        url_list.append(url_eve)
    # print(url_list)
    return url_list
# one_page()

def two_page():
    urls = one_page()
    for url in urls:
        user_info = {}
        htmll = requests.get(url, headers=get_headers())
        htmll.encoding = "UTF-8"
        html = htmll.text
        temps = etree.HTML(html)
        user_info['wx'] = ''.join(temps.xpath("//div[@class='count clearfix']/ul/li[2]/span/text()"))
        user_info['nickname'] = ''.join(temps.xpath("//div[@class='detail']/h1/text()"))
        user_info['qq'] = ''.join(temps.xpath("//div[@class='count clearfix']/ul/li[3]/span/text()"))
        # user_info['fans'] = ''.join(temps.xpath("//div[@class='count clearfix']/ul/li[1]/span/text()"))
        user_info['third_id'] = 'ws_' + user_info['wx']
        head = ''.join(temps.xpath("//div[@class='pic_show']/img/@src"))
        base_url = 'http://www.lyjlgs.com'
        headImage_url = base_url + head
        if os.path.isfile('%s' % user_info['third_id'] + '.png'):
            pass
        else:
            with open('%s' % user_info['third_id'] + '.png', 'wb') as f:
                img = requests.get(headImage_url).content
                f.write(img)
        print(user_info)
        mongo_info_wx.insert_item(user_info)

two_page()


