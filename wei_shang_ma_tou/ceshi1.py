# coding: utf-8

import pprint
import pymysql
import requests
import json


def get_ProxId():
    cate_url = "http://wsv1.fuguizhukj.cn/api/AttractFansProxy/ListFansProxyV4"
    headers = {
        'user-agent': 'Dart/2.7 (dart:io)',
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'content-length': '152',
        'host': 'wsv1.fuguizhukj.cn',
        'Connection': 'close',
        'Connection': 'close',
    }
    data = {"Tag": "其他", "PageNo": 1, "ItemPerPage": 100, "InnerVersion": "315", "ProductId": "63",
            "ChannalId": "88003", "ChannelId": "88003", "Version": "3.1.5", "pid": "63"}
    res = json.loads(requests.post(cate_url, headers=headers, data=json.dumps(data)).text)
    for detail_info in res['FansProxyItems']:
        detail_info_dict = {}
        detail_info_dict['Title'] = detail_info['Title']
        detail_info_dict['Tags'] = detail_info['Tags']
        detail_info_dict['PhoneNumber'] = detail_info['PhoneNumber']
        detail_info_dict['WechatNo'] = detail_info['WechatNo']
        pprint.pprint(detail_info_dict)

        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root",
                               database="gong_xiang_hy",
                               charset="utf8mb4")
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO ws_matou_huoyuan (Title, Tags, PhoneNumber, WechatNo) VALUE ('%s','%s','%s','%s')"
            base = (detail_info_dict['Title'], detail_info_dict['Tags'], detail_info_dict['PhoneNumber'],
                    detail_info_dict['WechatNo'])
            cursor.execute(sql % base)
            conn.commit()
        except:
            conn.rollback()
        conn.close()


get_ProxId()
