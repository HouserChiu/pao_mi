# coding: utf-8

import random
import pymysql
import requests
import pprint
import json
import urllib3
from headers_list import zone_headers, cate_headers, shop_id_headers, detail_headers
from params_list import zone_params, cate_params, shop_id_params, detail_params
import time
import math


# 获取地区代码
def get_zone():
    zone_url = "https://api.amoeba-inc.com/v4"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    zone_res = json.loads(requests.get(zone_url, params=zone_params(), headers=zone_headers(), verify=False).text)
    for province in zone_res['data']:
        for city in province['sites']:
            yield city['zdid']


# 获取类别信息的id
def get_cate(site_id):
    print(site_id)
    cate_url = "https://api.amoeba-inc.com/v4"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    cate_json = json.loads(
        requests.get(cate_url, headers=cate_headers(), params=cate_params(site_id), verify=False).text)
    for cate_ids in cate_json['data']:
        yield cate_ids['id']


# 获取店铺的id
def get_shop_id(market_id):
    print(market_id)
    shop_id_url = "https://api.amoeba-inc.com/v4"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    shop_id_res = json.loads(
        requests.get(shop_id_url, headers=shop_id_headers(), params=shop_id_params(market_id, 1), verify=False).text)

    for cpage in range(1, math.ceil(int(shop_id_res['data']['total']) / 100) + 1):
        shop_id_url1 = "https://api.amoeba-inc.com/v4"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        shop_id_res1 = json.loads(
            requests.get(shop_id_url1, headers=shop_id_headers(), params=shop_id_params(market_id, cpage),
                         verify=False).text)
        for shop_ids in shop_id_res1['data']['items']:
            yield shop_ids['shop_id']


# 获取详细信息
def get_detail(shop_id):
    print(shop_id)
    detail_url = "https://api.amoeba-inc.com/v4"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    detail_res = json.loads(
        requests.get(detail_url, headers=detail_headers(), params=detail_params(shop_id), verify=False).text)
    store_info_dict = {}
    store_info_dict['title'] = detail_res['data']['shop_name']
    store_info_dict['phone'] = detail_res['data']['phone']
    store_info_dict['wechat'] = detail_res['data']['wechat']
    store_info_dict['cate'] = detail_res['data']['main_cate_name']
    pprint.pprint(store_info_dict)
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root",
                           database="gong_xiang_hy",
                           charset="utf8mb4")
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO huo_yuan (title, phone, wechat, cate) VALUE ('%s','%s','%s','%s')"
        base = (
            store_info_dict['title'], store_info_dict['phone'], store_info_dict['wechat'], store_info_dict['cate'])
        cursor.execute(sql % base)
        conn.commit()
    except:
        conn.rollback()
    conn.close()


def main():
    zone_list = get_zone()
    for site_id in zone_list:
        sleep_time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        time.sleep(random.choice(sleep_time))
        for market_id in get_cate(site_id):
            sleep_time = [0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0]
            time.sleep(random.choice(sleep_time))
            for shop_id in get_shop_id(market_id):
                get_detail(shop_id)
                sleep_time = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
                time.sleep(random.choice(sleep_time))


if __name__ == '__main__':
    main()
