# -*- coding: utf-8 -*-

import hmac
import pprint
import time
import hashlib

import requests


def get_signKey():
    timestamp = str(int(time.time()))
    # data = '{"city":"成都市","latitude":30.64857,"longitude":104.08359,"address":"西部国际金融中心","coordType":"2","channelId":"4038","appVersion":"7.7.0","platform":"2","currentPage":1,"pageSize":10,"areaCode":1930,"ref":"home","ctp":"channel"}' + hashlib.md5(
    #     timestamp.encode("utf-8")).hexdigest()
    data = '{"city":"成都市","latitude":30.64857,"longitude":104.08359,"address":"西部国际金融中心","coordType":"2","channelId":"4038","appVersion":"7.7.0","platform":"2","currentPage":1,"pageSize":10,"areaCode":1930,"ref":"home","ctp":"channel"}' + '923047ae3f8d11d8b19aeb9f3d1bc002'
    eve_data = hashlib.md5(data.encode("utf-8")).hexdigest()
    # print(eve_data)
    return eve_data


# get_signKey()




def get_signkeyV1():
    appsecret = "61cd50a0cf384558afdb71410c65e065".encode('utf-8')  # 秘钥
    traceId = 'aa512bcb10cbe3f9ce0885eefe758de1' + '%s' % int(round(time.time() * 1000)) + '%s' % (int(round(time.time() * 1000)) - 2612463)
    data = ('5e5e2620622f1cac&Paidaojia&7.7.0&{"city":"成都市","latitude":30.64857,"longitude":104.08359,"address":"西部国际金融中心","coordType":"2","channelId":"4038","appVersion":"7.7.0","platform":"2","currentPage":1,"pageSize":10,"areaCode":1930,"ref":"home","ctp":"channel"}&360&baidu&1930&aa512bcb10cbe3f9ce0885eefe758de1&1605-A01&aa512bcb10cbe3f9ce0885eefe758de1&360&862490032087769&30.64857&30.64857&104.08359&104.08359&WIFI&baidu&android&7.1.1&西部国际金融中心&1080*1920&' + '%s' % get_signKey() + '&7.7.0.2&' + '%s' % int(round(time.time() * 1000)) + '&' + traceId)
    data_eve = data.encode('utf-8')  # 加密数据
    # print(data)
    # data = '5e5e2620622f1cac&Paidaojia&7.7.0&{"city":"成都市","latitude":30.64857,"longitude":104.08359,"address":"西部国际金融中心","coordType":"2","channelId":"4038","appVersion":"7.7.0","platform":"2","currentPage":1,"pageSize":10,"areaCode":1930,"ref":"home","ctp":"channel"}&360&baidu&1930&aa512bcb10cbe3f9ce0885eefe758de1&1605-A01&aa512bcb10cbe3f9ce0885eefe758de1&360&862490032087769&30.64857&30.64857&104.08359&104.08359&WIFI&baidu&android&7.1.1&西部国际金融中心&1080*1920&4039f1736f251c5b41a900e27a300183&7.7.0.2&1597052396463&aa512bcb10cbe3f9ce0885eefe758de115970497841931597052396454'.encode('utf-8')
    signature = hmac.new(appsecret, data_eve, digestmod=hashlib.sha256).hexdigest()
    # print(signature)
    return signature, traceId


# get_signkeyV1()


def get_data():
    url = "https://gw-o2o.jddj.com/client"
    headers = {
        'Host': 'gw-o2o.jddj.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0',
    }
    params = {
        'deviceId': 'aa512bcb10cbe3f9ce0885eefe758de1',
        'city_id': '1930',
        'signKeyV1': '%s' % get_signkeyV1()[0],
        'screen': '1080*1920',
        'signKey': '%s' % get_signKey(),
        'androidId': '5e5e2620622f1cac',
        'deviceToken': 'aa512bcb10cbe3f9ce0885eefe758de1',
        't': '%s' % int(round(time.time() * 1000)),
        # 't': '1597052396463',
        'appVersion': '7.7.0',
        'imei': '862490032087769',
        # 'traceId': 'aa512bcb10cbe3f9ce0885eefe758de115970497841931597052396454',
        'traceId': '%s' % get_signkeyV1()[1],
        # 'traceId': 'aa512bcb10cbe3f9ce0885eefe758de1' + '%s' % int(round(time.time() * 1000)) + '%s' % int(round(time.time() * 1000)),
        'deviceModel': '1605-A01',
        'poi': '西部国际金融中心',
        'lng_pos': '104.08359',
        'channel': 'baidu',
        'networkType': 'WIFI',
        'functionId': 'zone/recommendStoreList',
        'devideModel': '360',
        'body': '{"city":"成都市","latitude":30.64857,"longitude":104.08359,"address":"西部国际金融中心","coordType":"2","channelId":"4038","appVersion":"7.7.0","platform":"2","currentPage":1,"pageSize":10,"areaCode":1930,"ref":"home","ctp":"channel"}',
        'appName': 'Paidaojia',
        'lng': '104.08359',
        'platVersion': '7.1.1',
        'brand': '360',
        'subVersion': '7.7.0.2',
        'partner': 'baidu',
        'lat': '30.64857',
        'platCode': 'android',
        'lat_pos': '30.64857',
    }
    res = requests.get(url, params=params, headers=headers, verify=False).text
    pprint.pprint(res)
get_data()
