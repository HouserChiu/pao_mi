# coding: utf-8

import requests
import pprint
import json

def get_cate():
    url1 = "https://api.pinduoduo.com/api/search/operation/detail/group"
    params = {
        'engine_version': '2.0',
        'opt_id': '10364',
        'link_id': '77dc41d1-a751-42bb-9de0-532e441fe69d',
        'page_id': 'classification.html',
        'pdduid': '4276569950116',
    }
    headers = {
        'Referer': 'Android',
        'X-PDD-QUERIES': 'width=1080&height=1920&net=1&brand=360&model=1605-A01&osv=7.1.1&appv=5.24.0&pl=2',
        'ETag': 'JqAGclY0',
        'Content-Type': 'application/json;charset=UTF-8',
        'AccessToken': 'WS77LGNWVFPBJCLNP5AOMVM7WMTDY4NIF4SVAFVAHCZNO64PXALA113a4ac',
        'p-appname': 'pinduoduo',
        'x-b3-ptracer': 'httpCall39ed8966209148e18f96d883',
        'User-Agent': 'android Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36  phh_android_version/5.24.0 phh_android_build/9775e3c85deff9134a0362f3bbe63ecb18d4e379 phh_android_channel/qihu360 pversion/0',
        'PDD-CONFIG': 'V4:001.052400',
        'Host': 'api.pinduoduo.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Cookie': 'acid=5b53359335f4709b9c25dcb3eddb0b54; JSESSIONID=AF9E3A93D069D214D36BAA2052B99082; api_uid=CiXgE18jwU5dbwBNC+rzAg==',
    }
    res1 = requests.get(url1, params=params, headers=headers, verify=False).text
    pprint.pprint(res1)

get_cate()