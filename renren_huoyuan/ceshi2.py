# coding: utf-8
import pymysql
import requests
import json
import urllib3
import pprint
import math


def get_result():
    result_url = "https://www.techzk.com/api/Cms/ShopList"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'user-agent': 'MI 9(Android/5.1.1) (com.techzk.hybao/1.0) Weex/0.26.0 1080x1920',
        'Host': 'www.techzk.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Length': '110',
    }
    data = {"n": "ShopList", "q": {"a": 3}, "s": "659f29cdcc84d8a2a7c85afd0c3ad9b8"}
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = json.loads(requests.post(result_url, headers=headers, verify=False, data=json.dumps(data)).text)
    for detail_res in res['q']['shops']:
        store_info_dict = {}
        store_info_dict['name'] = detail_res['name']
        store_info_dict['mobile'] = detail_res['mobile']
        store_info_dict['wechat'] = detail_res['wechat']
        store_info_dict['categoryNames'] = detail_res['categoryNames'][0]
        pprint.pprint(store_info_dict)
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root",
                               database="gong_xiang_hy",
                               charset="utf8mb4")
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO ren_ren_huoyuan (name, mobile, wechat, categoryNames) VALUE ('%s','%s','%s','%s')"
            base = (
                store_info_dict['name'], store_info_dict['mobile'], store_info_dict['wechat'],
                store_info_dict['categoryNames'])
            cursor.execute(sql % base)
            conn.commit()
        except:
            conn.rollback()
        conn.close()


get_result()
