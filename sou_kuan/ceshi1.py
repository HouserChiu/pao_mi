# coding: utf-8
import random
import time
import pymysql
import requests
import json
import pprint
import urllib3

def page_one():
    headers = {
        'device-token': 'AjWkdU6ROK1wHc0MSYpj-BlZTqhqZF-FcPB2zLxD5JdK',
        'device-type': '360+1605-A01',
        'device-net': '3',
        'device-lat': '30.654303',
        'city': 'gz',
        'device-channel': '3',
        'device-address': '%E4%B8%AD%E5%9B%BD%E5%9B%9B%E5%B7%9D%E7%9C%81%E6%88%90%E9%83%BD%E5%B8%82%E9%94%A6%E6%B1%9F%E5%8C%BA%E6%B8%85%E5%AE%89%E8%A1%9782%E5%8F%B7',
        'os': '2',
        'device-size': '1080*1920',
        'app-version': '3.7.0',
        'device-id': 'c25b9bb5c0032fc0865c1e2bdeef133b',
        'secret': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ2dmljX2FuZHJvaWQiLCJleHAiOjE1OTk0Njc1NzIsImlzcyI6InZ2aWMuY29tIn0.gSQ4X5sKzEhmImrbqq-o4j_r0PmBInHShqb-6alpP4Q',
        'device-type2': '2',
        'device-lang': 'zh_CN',
        'device-version': '7.1.1',
        'device-lon': '104.090268',
        'cityId': '1',
        'device-ip': '172.27.35.3',
        'registerSource': '0',
        'Host': 'app.vvic.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.1',
    }
    url = "https://app.vvic.com/v1/shop-list"
    for page in range(988, 1549):
        print('++' + str(page))
        params = {
            'currentPage': '%s' % page,
            'pageSize': '10',
            'secret': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ2dmljX2FuZHJvaWQiLCJleHAiOjE1OTk0Njc1NzIsImlzcyI6InZ2aWMuY29tIn0.gSQ4X5sKzEhmImrbqq-o4j_r0PmBInHShqb-6alpP4Q',
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = json.loads(requests.get(url, params=params, headers=headers, verify=False).text)
        for id_info in res['data']['recordList']:
            yield id_info['shopId']


def page_two(shopId):
    headers1 = {
        'device-token': 'AjWkdU6ROK1wHc0MSYpj-BlZTqhqZF-FcPB2zLxD5JdK',
        'device-type': '360+1605-A01',
        'device-net': '3',
        'device-lat': '30.654303',
        'city': 'gz',
        'device-channel': '3',
        'device-address': '%E4%B8%AD%E5%9B%BD%E5%9B%9B%E5%B7%9D%E7%9C%81%E6%88%90%E9%83%BD%E5%B8%82%E9%94%A6%E6%B1%9F%E5%8C%BA%E6%B8%85%E5%AE%89%E8%A1%9782%E5%8F%B7',
        'os': '2',
        'device-size': '1080*1920',
        'app-version': '3.7.0',
        'device-id': 'c25b9bb5c0032fc0865c1e2bdeef133b',
        'secret': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ2dmljX2FuZHJvaWQiLCJleHAiOjE1OTk0NjkyMTcsImlzcyI6InZ2aWMuY29tIn0.F-RZMa1tuOPPV8aMyLAbmstO7QATIroZ-GqfYq3-bM0',
        'device-type2': '2',
        'device-lang': 'zh_CN',
        'device-version': '7.1.1',
        'device-lon': '104.090268',
        'cityId': '1',
        'device-ip': '172.27.35.3',
        'registerSource': '0',
        'Host': 'app.vvic.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.1',
    }
    url1 = "https://app.vvic.com/v1/shop"
    params1 = {
        'id': '%s' % shopId,
        'merge': '0',
        'orderby': 'up_time',
        'pageSize': '12',
        'secret': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ2dmljX2FuZHJvaWQiLCJleHAiOjE1OTk0NjkyMTcsImlzcyI6InZ2aWMuY29tIn0.F-RZMa1tuOPPV8aMyLAbmstO7QATIroZ-GqfYq3-bM0',
        'sort': 'desc',
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res1 = json.loads(requests.get(url1, headers=headers1, params=params1, verify=False).text)
    store_info_dict = {}
    store_info_dict['shop_name'] = res1['data']['shop']['shop_name']
    store_info_dict['wechat'] = res1['data']['shop']['wechat']
    store_info_dict['telephone'] = res1['data']['shop']['telephone']
    try:
        store_info_dict['primary_cate'] = res1['data']['shop']['primary_cate']
    except KeyError:
        store_info_dict['primary_cate'] = ''
    pprint.pprint(store_info_dict)
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root",
                           database="gong_xiang_hy",
                           charset="utf8mb4")
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO sou_kuan (shop_name, wechat, telephone, primary_cate) VALUE ('%s','%s','%s','%s')"
        base = (
            store_info_dict['shop_name'], store_info_dict['wechat'], store_info_dict['telephone'], store_info_dict['primary_cate'])
        cursor.execute(sql % base)
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def main():
    shop_id_list = page_one()
    sleep_time = [0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0]
    time.sleep(random.choice(sleep_time))
    for shop_id in shop_id_list:
        page_two(shop_id)

if __name__ == '__main__':
    main()

