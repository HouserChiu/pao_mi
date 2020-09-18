# coding: utf-8
import os
import time

from mongo_info import mongo_info_wd
import requests
import json
import urllib3
import urllib.parse

def get_headers():
    headers = {
        'Host': 'thor.weidian.com',
        'Connection': 'keep-alive',
        'Content-Length': '145',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://h5.weidian.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36  WDAPP(WD/9.1.25) appid/com.koudai.weishop KDJSBridge2/1.1.0 platform/android apiv/91250 NetType/WIFI',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://h5.weidian.com/m/fxdaka/index.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'Cookie': 'wdtoken=f508c60e; login_token=_EwWqqVIQIILz2Pttxz80ydJ4nZEmK1YEWEdnZpdCXilMI1Yf6rHAD41v6TkHIdh5XgxhVkCOS2-o6xnQlfp4jcapsAV0Z0zn61umm2Plr9n20wSKG0q4CxXmqHDwnVFJ3bFpmTD1vR2YbM-8rtTskTjbDeSZK7AwRZcuHcu4ecdo8oyAxDg; is_login=true; login_type=LOGIN_USER_TYPE_MASTER; login_source=LOGIN_USER_SOURCE_MASTER; uid=1497239663; duid=1497239663; sid=1767898276; __spider__visitorid=5c4cb1c0ca2b6bed497c9ca96b404b6a; __spider__sessionid=8431ebcf9d2b956f',
        'X-Requested-With': 'com.koudai.weishop',
    }
    return headers


def get_detail():
    for i in range(1, 6):
        data = '{"sortField":"monthSellAmount","sortType":"desc","tags":[],"pageNum":%s,"pageSize":20}' % i
        url = 'https://thor.weidian.com/fxbiz/daka.list/1.0'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = json.loads(requests.post(url, data=('param=' + urllib.parse.quote(data)), headers=get_headers(), verify=False).text)
        for temp in res['result']:
            user_info = {}
            user_info['网红昵称'] = temp['detail']['leaderName']
            user_info['头像'] = temp['detail']['kaSellerImg']
            user_info['联系微信'] = temp['detail']['weChatId']
            user_info['id'] = temp['detail']['sellerId']
            user_info['签名'] = temp['detail']['leaderComment']
            user_info['第三方ID'] = 'wd_' + user_info['id']

            if os.path.isfile('%s' % user_info['第三方ID'] + '.jpg'):
                pass
            else:
                with open('%s' % user_info['第三方ID'] + '.jpg', 'wb') as f:
                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    img = requests.get(user_info['头像'], verify=False).content
                    f.write(img)
            print(user_info)

            mongo_info_wd.insert_item(user_info)
            time.sleep(2)

get_detail()
