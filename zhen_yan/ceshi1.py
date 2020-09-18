# coding: utf-8
import datetime
import time
import requests
import hashlib
def spider():
    url = 'https://app.suzhou-news.cn/api/v1/appNews/getBannerGuideNewsList?bannerID=32'
    # uuid = 'IMEI865166022143641-IMSI460009616510363'

    ll_csi = '{"android":{"market":"_360","mac":""},"platform":"Android","resolution":{"w":1080,"h":1920,"s":3},"brand":"vivo","model":"V1923A","ov":"5.1.1","av":"1.1.40","lang":"zh","currTime":"2020-07-17T01:48:11Z"}'
    ll_ukn = '1RdM6030J3MoXpkNeROGQ3y4yLkeZWQp99vK/D2aNG2KaUMmnCCsCZwVOnENeKiqQmwoYRZZu9JvCAUIErDHUA=='
    ll_pln = '{"id":32704,"phone":"18391726137","nick":"James","sex":"Male"}'
    encrypt = f"https://a2.liao4fun.com/LoadUsersNew&&{ll_ukn}&&{ll_csi}&&{ll_pln}"
    signature = hashlib.md5(encrypt.encode("utf-8")).hexdigest()
    print(signature)
    # headers = {
    #     'accept': 'application/json',
    #     'll_csi': '{"android":{"market":"_360","mac":""},"platform":"Android","resolution":{"w":900,"h":1600,"s":2},"brand":"Android","model":"MI%209","ov":"5.1.1","av":"1.1.40","lang":"zh","currTime":"' + '%s' % (datetime.datetime.now()).strftime('%Y-%m-%d') + 'T' + '%s' % ((datetime.datetime.now()) + datetime.timedelta(hours=-8)).strftime('%H:%M:%S') + 'Z"}',
    #     'll_ukn': '1RdM6030J3MoXpkNeROGQ3y4yLkeZWQp99vK/D2aNG2KaUMmnCCsCZwVOnENeKiqQmwoYRZZu9JvCAUIErDHUA==',
    #     'll_pln': '{"id":32704,"phone":"18391726137","nick":"James","sex":"Male"}',
    #     'll_legal': '%s' % signature,
    #     'Content-Type': 'application/json',
    #     'Content-Length': '179',
    #     'Host': 'a2.liao4fun.com',
    #     'Connection': 'Keep-Alive',
    #     'Accept-Encoding': 'gzip',
    #     'User-Agent': 'okhttp/3.12.1',
    # }
    # res = requests.get(url, headers=headers, verify=False).text
    # print(res)
spider()