# coding: utf-8
'''
行业排行榜
'''
import pymysql
import requests
import datetime
from lxml import etree

def get_headers():
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "ASP.NET_SessionId=uayu5bmrg1bazdfx0kbuwctp; _uab_collina=159228833043839902377315; Qs_lvt_194035=1592288331; mediav=%7B%22eid%22%3A%22163230%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22E')Es-VNJ%3D91Ny%3CtDoi(%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22E')Es-VNJ%3D91Ny%3CtDoi(%22%7D; Hm_lvt_91a409c98f787c8181d5bb8ee9c535ba=1592288331; XIGUADATA=UserId=53a26cf2225351b6&checksum=26b128c6d4dd&XIGUADATALIMITID=9ff992ffc4824624a45132331d7857c0; UserUnionId=86699e75c128037646736ed5de2da9c5bc081cdcc32ed85a14890d1c4ea9bf99; systemupdatenotice=75; compareArray=[]; xiguadata_advertise_survey=xiguadata_advertise_survey; Qs_pv_194035=3789831667952099300%2C3662121152619942000%2C2883851125221819000%2C744489643626861800%2C3532217017102112300; Hm_lpvt_91a409c98f787c8181d5bb8ee9c535ba=1592291172",
        "Host": "data.xiguaji.com",
        "Referer": "http://data.xiguaji.com/Home",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    return headers

def get_cat():
    url = 'http://data.xiguaji.com/rank/IndustryNew'
    temp = requests.get(url, headers=get_headers()).text
    cat_list = []
    for tag in etree.HTML(temp).xpath("//div[@id='js-id-industry']/span/a"):
        eve = ''.join(tag.xpath("./@ data-categoryid"))
        cat_list.append(eve)
    # print(cat_list)
    return cat_list

def get_params():
    ids = get_cat()
    params_list = []
    for id in ids:
        params = {
            'tid': '%s' % id ,
            'pageIndex': '1',
            'isPart': 'true',
            'period': '1',
            'statDateCode': '%s' % (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y%m%d'),
            'menuClick': 'true',
        }
        params_list.append(params)
    return params_list

def get_one():
    params_list = get_params()
    bizid_lists = []
    key_lists = []
    for params in params_list:
        url = 'http://data.xiguaji.com/rank/IndustryNew/'
        res = requests.get(url, params=params, headers=get_headers()).text
        trs = etree.HTML(res)
        bizid_list = []
        key_list = []
        for tr in trs:
            bizid = ''.join(tr.xpath(".//span[@class='js-rank-detail-btn']/@data-bizid"))
            key = ''.join(tr.xpath(".//span[@class='js-rank-detail-btn']/@data-key"))
            bizid_list.append(bizid)
            key_list.append(key)
        bizid_lists.append(bizid_list)
        key_lists.append(key_list)
    return bizid_lists, key_lists

def get_two():
    bizidss = get_one()[0]
    keyss = get_one()[1]
    for bizids, keys in zip(bizidss, keyss):
        for bizid, key in zip(bizids, keys):
            params = {
                'bizId': '%s' % bizid,
                'key': '%s' % key,
            }
            url = 'http://data.xiguaji.com/Search/Detail'
            res = requests.get(url, params=params, headers=get_headers()).text
            user_info = {}
            user_info['platform'] = '10'
            user_info['avatar'] = 'https:' + ''.join(etree.HTML(res).xpath("//div[@class='number-logo']/img/@src"))
            user_info['name'] = ''.join(etree.HTML(res).xpath("//div[@class='number-details']/h3/text()"))

            user_info['account'] = ''.join(etree.HTML(res).xpath("//div[@class='btns-group']/a[2]/@data-wid"))
            user_info['categoryid'] = ''.join(etree.HTML(res).xpath("//div[@class='function-decribe']/p[1]/text()")).strip()
            if ''.join(etree.HTML(res).xpath("//div[@class='function-decribe']/p[2]/text()")).strip() == '--':
                user_info['location'] = ''
            else:
                user_info['location'] = ''.join(etree.HTML(res).xpath("//div[@class='function-decribe']/p[2]/text()")).strip()
            if ''.join(etree.HTML(res).xpath("//div[@class='similar-publicnum']/p/text()")).strip() == "个人":
                user_info['mcn'] = ''
            else:
                user_info['mcn'] = ''.join(etree.HTML(res).xpath("//div[@class='similar-publicnum']/p/text()")).strip()
            fans = ''.join(etree.HTML(res).xpath("//ul[@class='recent-statistics-chart clearfix']/li[1]/text()")).strip()
            if '万' in fans:
                user_info['fans'] = int(float(fans.split('万')[0]) * 10000)
            else:
                user_info['fans'] = ''.join(etree.HTML(res).xpath("//ul[@class='recent-statistics-chart clearfix']/li[1]/text()")).strip()
            user_info['production'] = ''.join(etree.HTML(res).xpath("//ul[@class='recent-statistics-chart clearfix']/li[2]/text()")).strip()
            user_info['signature'] = ''.join(etree.HTML(res).xpath("//p[@class='p-biz-desc']/text()")).strip()
            user_info['age'] = ''
            user_info['likes'] = ''
            user_info['label'] = ''
            user_info['stars'] = ''
            user_info['sex'] = ''
            user_info['url'] = ''
            user_info['userid'] = bizid
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

get_two()


















