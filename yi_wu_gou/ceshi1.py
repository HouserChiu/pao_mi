# coding: utf-8
import random
import time
import pymysql
import requests
import pprint
from headers_list import one_cate_headers, two_cate_headers, detail_headers
import json
import urllib3
import math


def get_one_cate():
    cate_one_url = "https://app.yiwugo.com/en/producttype/listforapp.html"
    data = {
        'webtype': 'cn'
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    one_cate_res = requests.post(cate_one_url, data=data, headers=one_cate_headers(), verify=False).text
    one_cate_json = json.loads(one_cate_res)
    for one_cate_ids in one_cate_json['list']:
        yield one_cate_ids['id']


def get_two_cate(one_cate_id):
    cate_two_url = "https://app.yiwugo.com/en/producttype/listforapp.html"
    params = {
        'uppertype': '%s' % one_cate_id,
        'webtype': 'cn',
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    two_cate_res = requests.get(cate_two_url, params=params, headers=two_cate_headers(), verify=False).text
    two_cate_json = json.loads(two_cate_res)
    for two_cate_ids in two_cate_json['list']:
        yield two_cate_ids['type']


def get_detail(two_cate_id):
    # 获取页数
    params1 = {
        'appid': '1',
        'areacode': '10',
        'q': '%s' % two_cate_id,
        'cpage': '1',
        'pageSize': '28',
    }
    detail_url1 = "https://app.yiwugo.com/search/sshop.htm"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    detail_res1 = requests.get(detail_url1, headers=detail_headers(), params=params1, verify=False).text
    detail_json1 = json.loads(detail_res1)
    # 向上取整
    for page in range(1, math.ceil(int(detail_json1['numfound']) / 28) + 1):
        params = {
            'appid': '1',
            'areacode': '10',
            'q': '%s' % two_cate_id,
            'cpage': '%s' % page,
            'pageSize': '28',
        }
        detail_url = "https://app.yiwugo.com/search/sshop.htm"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        detail_res = requests.get(detail_url, headers=detail_headers(), params=params, verify=False).text
        detail_json = json.loads(detail_res)

        if detail_json['resultlist'] != []:
            for store_info in detail_json['resultlist']:
                store_info_dict = {}
                store_info_dict['title'] = store_info['shopName']
                store_info_dict['phone'] = store_info['mobile']
                store_info_dict['cate'] = two_cate_id
                pprint.pprint(store_info_dict)

                conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root",
                                       database="gong_xiang_hy",
                                       charset="utf8mb4")
                cursor = conn.cursor()
                try:
                    sql = "INSERT INTO yi_wu_gou (title, phone, cate) VALUE ('%s','%s','%s')"
                    base = (
                        store_info_dict['title'], store_info_dict['phone'], store_info_dict['cate'])
                    cursor.execute(sql % base)
                    conn.commit()
                except:
                    conn.rollback()
                conn.close()
        sleep_time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        time.sleep(random.choice(sleep_time))

def main():
    one_cate_list = get_one_cate()
    for one_cate in one_cate_list:
        two_cate_list = get_two_cate(one_cate)
        sleep_time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        time.sleep(random.choice(sleep_time))
        for two_cate in two_cate_list:
            get_detail(two_cate)
            sleep_time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
            time.sleep(random.choice(sleep_time))


if __name__ == '__main__':
    main()
