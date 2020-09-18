# coding: utf-8

import time
import requests
import hashlib
def ylb():
    url = 'https://app.suzhou-news.cn/api/v1/appNews/getBannerGuideNewsList?bannerID=32'
    uuid = 'IMEI865166022143641-IMSI460009616510363'
    timestamp = str(int(time.time()))
    encrypt = f"{uuid}&&{timestamp}&&f1190aca-d08e-4041-8666-29931cd89dde"
    signature = hashlib.md5(encrypt.encode("utf-8")).hexdigest()
    headers = {
        'sys': 'Android',
        'sysVersion': '5.1.1',
        'appVersion': '7.6',
        'udid': 'IMEI865166022143641-IMSI460009616510363',
        'clientType': 'android',
        'timestamp': '%s' % str(int(time.time())),
        'signature': '%s' % signature,
        'Host': 'app.suzhou-news.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.4.1',
    }
    res = requests.get(url, headers=headers, verify=False).text
    print(res)
ylb()
