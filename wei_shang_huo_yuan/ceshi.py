# coding: utf-8
import json

import pymysql
import requests
import pprint


def get_headers():
    url = "http://wsv1.fuguizhukj.cn/api//UserCard/ListUserCard"
    headers = {
        'user-agent': 'Dart/2.7 (dart:io)',
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'content-length': '79',
        'host': 'wsv1.fuguizhukj.cn',
        'Connection': 'close',
        'Connection': 'close',
    }
    data = {"CurrentPage":11,"ItemPerPage":20,"InnerVersion":"104","ProductId":"63","ChannalId":"124005","Version":"1.0.4"}
    res = json.loads(requests.post(url, headers=headers, verify=False, data=json.dumps(data)).text)
    # print(res)
    for detail_info in res['UserCardDetailList']:
        detail_info_dict = {}
        detail_info_dict['Title'] = detail_info['NickName']
        detail_info_dict['Tags'] = detail_info['Tags']
        detail_info_dict['PhoneNumber'] = detail_info['Phone']
        detail_info_dict['WechatNo'] = detail_info['WechatName']
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


get_headers()
