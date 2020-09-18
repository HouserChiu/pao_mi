import datetime
import re
import time
import pymysql
import requests
import json
import urllib3
from lxml import etree


def get_headers():
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'visitor_type=old; acw_tc=76b20fe415904773946027228e1fce32e1d2271a3c88b32ea5d521950d3286; 53gid2=11033499737004; 53revisit=1590477397155; 53gid1=11033499737004; qbad=1; _gsdataCL=WzAsIjE3NzI2NDU0MjM2IiwiMjAyMDA2MDQxMTQxNTgiLCIwYTY2NjA2ZTBiYzA0OGFjNGIyNjAzODk5OWZiZWM0MSIsMzAxNTM0XQ%3D%3D; _gsdataOL=301534%3B17726454236%3B%7B%220%22%3A%22%22%2C%221%22%3A%22%22%2C%222%22%3A%22%22%2C%223%22%3A%22%22%2C%224%22%3A%22%22%2C%225%22%3A%22%22%2C%2299%22%3A%2220200604%22%7D%3B32d52f3ad22d853641b622186a188471; _identity-frontend=c011cc66e3ed8df0e49c28fcae7e51320e5389ce7248dd046b1923f0ddc5d56ba%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A28%3A%22%5B%22609049%22%2C%22test+key%22%2C604800%5D%22%3B%7D; PHPSESSID=nttg6n0u4v1aivo6feabpkg1v0; _csrf-frontend=4ec7a30b4d9705e2af0c224cc44d162424aff75dc258d6908c187bfaa788db50a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22rL_1IHYPXWYlDlBworhV7oilmHEzJN_n%22%3B%7D; visitor_type=old; 53gid0=11033499737004; 53kf_72213613_from_host=www.gsdata.cn; 53kf_72213613_land_page=http%253A%252F%252Fwww.gsdata.cn%252F; kf_72213613_land_page_ok=1; Hm_lvt_293b2731d4897253b117bb45d9bb7023=1590477397,1591242090,1591320829; 53uvid=1; onliner_zdfq72213613=0; 53kf_72213613_keyword=http%3A%2F%2Fwww.gsdata.cn%2F; Hm_lpvt_293b2731d4897253b117bb45d9bb7023=' + '%s' % str(
            int(time.time())),
        'Host': 'www.gsdata.cn',
        'Referer': 'http://www.gsdata.cn/rank/wxrank',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    return headers

def get_cate():
    url = 'http://www.gsdata.cn/rank/wxrank'
    res = requests.get(url,headers=get_headers()).text
    temp = etree.HTML(res).xpath("//ul[@class='dropdown-menu more']/li")
    cate_list = []
    for cate in temp:
        cate_list.append(''.join(cate.xpath("./a/@data-value")))
    # print(cate_list)
    return cate_list

# get_cate()

def get_params():
    cates = get_cate()
    cate_list = []
    for cate in cates:
        params = [
            {'type': 'day', 'post_time': '%s' % (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d'), 'page': '1', 'types': '%s' % cate, 'industry': 'all', 'proName': '',
             'industry_full': 'all', 'proName_full': '', 'dataType': 'json', },
            {'type': 'day', 'post_time': '%s' % (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d'), 'page': '2', 'types': '%s' % cate, 'industry': 'all', 'proName': '',
             'industry_full': 'all', 'proName_full': '', 'dataType': 'json', },
            {'type': 'day', 'post_time': '%s' % (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d'), 'page': '3', 'types': '%s' % cate, 'industry': 'all', 'proName': '',
             'industry_full': 'all', 'proName_full': '', 'dataType': 'json', },
            {'type': 'day', 'post_time': '%s' % (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d'), 'page': '4', 'types': '%s' % cate, 'industry': 'all', 'proName': '',
             'industry_full': 'all', 'proName_full': '', 'dataType': 'json', },
        ]
        cate_list.append(params)
    # print(cate_list)
    return cate_list
# get_params()


def get_one():
    temp = get_params()
    url_lists = []
    for eve in temp:
        for params in eve:
            url = 'http://www.gsdata.cn/rank/ajax_wxrank'
            res = json.loads(requests.get(url, headers=get_headers(), params=params).text)
            try:
                html = etree.HTML(res['data'])
                url_list = []
                for wxid in html.xpath("//tr"):
                    url = 'http://www.gsdata.cn' + ''.join(wxid.xpath("./td[2]/a/@href"))
                    url_list.append(url)
                url_lists.append(url_list)
            except KeyError:
                pass
    return url_lists
    # print(url_lists)
# get_one()

def get_two():
    urlss = get_one()
    for urls in urlss:
        for url in urls:
            html = requests.get(url, headers=get_headers())
            html.encoding = "UTF-8"
            res = etree.HTML(html.text)
            user_info = {}
            user_info['platform'] = '6'
            user_info['avatar'] = re.search('<div.*?wxDetail-img fl.*?url\((.*?)\).*?</div>', html.text, re.S).group(1)
            user_info['userid'] = url.split('=')[1]
            user_info['name'] = ''.join(res.xpath("//label[@class='fs22']/text()"))
            user_info['url'] = ''
            user_info['location'] = ''.join(res.xpath("//div[@class='info-li clearfix']/div[2]/p[2]/text()"))
            user_info['account'] = ''.join(res.xpath("//div[@class='fl']/p[1]/text()"))
            user_info['sex'] = ''
            user_info['stars'] = ''
            user_info['personal_profile'] = ''.join(res.xpath("//div[@class='info-li clearfix']/p[1]/text()"))
            user_info['label'] = ''.join(res.xpath("//span[@class='tagLi']/a[1]/text()"))
            try:
                user_info['production'] = re.search('共.*?(\d+).*?章',''.join(res.xpath("//p[@class='cr7d']/text()")[-2])).group(1)
            except IndexError:
                user_info['production'] = ''

            user_info['age'] = ''
            user_info['mcn'] = ''.join(res.xpath("//div[@class='fl']/p[2]/text()"))
            user_info['categoryid'] = ''.join(res.xpath("//div[@class='info-li clearfix']/div[2]/p[1]/text()"))
            user_info['fans'] = ''
            try:
                user_info['likes'] = ''.join(res.xpath("//p[@class='fs28']/text()")[-3])
            except IndexError:
                user_info['likes'] = ''
            print(user_info)

            conn = pymysql.connect(host="111.231.0.33", port=3306, user="ceshi", password="ChaxunNewOtMySql1129",
                                   database="test",
                                   charset="utf8mb4")
            cursor = conn.cursor()
            try:
                sql = "INSERT INTO t_from_user_info (platform, avatar, userid, name, url, location, account, sex, stars, personal_profile, label, production, age, mcn, categoryid, fans, likes) VALUE ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                base = (user_info['platform'], user_info['avatar'], user_info['userid'], user_info['name'],
                        user_info['url'], user_info['location'], user_info['account'], user_info['sex'],
                        user_info['stars'], user_info['personal_profile'], user_info['label'],
                        user_info['production'], user_info['age'], user_info['mcn'], user_info['categoryid'],
                        user_info['fans'], user_info['likes'])
                cursor.execute(sql % base)
                conn.commit()
            except:
                conn.rollback()
            conn.close()

get_two()

