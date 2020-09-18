# coding: utf-8
import pprint

import pymysql
import requests
import json


def get_ProxId():
    recomm_url = "http://wsv1.fuguizhukj.cn/api/AttractFansProxy/ListProxyItemOnlineByTime"
    headers = {
        'user-agent': 'Dart/2.7 (dart:io)',
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'content-length': '139',
        'host': 'wsv1.fuguizhukj.cn',
        'Connection': 'close',
        'Connection': 'close',
    }
    # for i in range(1, 419):
    #     print(i)
    #     data = {"PageIndex": i, "ItemPerPage": 20, "InnerVersion": "315", "ProductId": "63", "ChannalId": "88003",
    #             "ChannelId": "88003", "Version": "3.1.5", "pid": "63"}
    #     res_id = json.loads(requests.post(recomm_url, headers=headers, data=json.dumps(data)).text)
    #     for temp_ProxId in res_id["ListProxyItems"]:
    #         yield temp_ProxId['ProxId']
    data = {"PageIndex": 419, "ItemPerPage": 20, "InnerVersion": "315", "ProductId": "63", "ChannalId": "88003",
            "ChannelId": "88003", "Version": "3.1.5", "pid": "63"}
    res_id = json.loads(requests.post(recomm_url, headers=headers, data=json.dumps(data)).text)
    for temp_ProxId in res_id["ListProxyItems"]:
        yield temp_ProxId['ProxId']


def get_detail(ProxId):
    detail_url = "http://wsv1.fuguizhukj.cn/api/AttractFansProxy/ProxyDetail"
    headers = {
        'user-agent': 'Dart/2.7 (dart:io)',
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'content-length': '125',
        'host': 'wsv1.fuguizhukj.cn',
        'Connection': 'close',
        'Connection': 'close',
    }
    data = {"ProxyId": "%s" % ProxId, "InnerVersion": "315", "ProductId": "63", "ChannalId": "88003",
            "ChannelId": "88003", "Version": "3.1.5", "pid": "63"}
    detail_info = json.loads(requests.post(detail_url, headers=headers, data=json.dumps(data)).text)
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

def main():
    ProxId_list = get_ProxId()
    for ProxId in ProxId_list:
        get_detail(ProxId)

if __name__ == '__main__':
    main()
