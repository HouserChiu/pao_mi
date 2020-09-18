# coding: utf-8
'''
电商分析，后续和主程序一起跑
'''
import time

import requests
import json
import datetime
import pymysql


def get_headers():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=utf-8',
        'Cookie': 'gr_user_id=2f55f746-df25-4729-b4a2-73e4f1249792; grwng_uid=7f374b19-3fc5-4dbe-b7af-a64d5feed898; __51cke__=; 8e22d1b16f393571_gr_session_id=30b44f43-b20a-4771-8aaa-6b3a24924eb5; 8e22d1b16f393571_gr_session_id_30b44f43-b20a-4771-8aaa-6b3a24924eb5=true; Hm_lvt_a135ef5290d5317a9a4a051b9fee8f92=1592790236,1592876531; JSESSIONID=91294985C55905766F509095BF5AC3AD; __tins__20450359=%7B%22sid%22%3A%201592876530943%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201592878359429%7D; __51laig__=3; Hm_lpvt_a135ef5290d5317a9a4a051b9fee8f92=1592876560',
        'Host': 'www.huo1818.com',
        'PC_OPEN_ID': 'oQ4u90T6S56IOfhGIj69huJ4CZO4',
        'Referer': 'http://www.huo1818.com/ranking/goods',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    return headers


def get_cate():
    url = 'http://www.huo1818.com/live-api/selector/tags'
    res = json.loads(requests.get(url, headers=get_headers()).text)
    cate_list = []
    for cate in res['result']:
        cate_list.append(cate['tag'])
    return cate_list


def get_params():
    cates = get_cate()
    cate_list = []
    for cate in cates:
        params = [
            {'tag': '%s' % cate, 'type': '1', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },
            {'tag': '%s' % cate, 'type': '8', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },
            {'tag': '%s' % cate, 'type': '9', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },


        ]
        cate_list.append(params)
    return cate_list


def get_one():
    temp = get_params()
    Id_lists = []
    for eve in temp:
        for params in eve:
            url = 'http://www.huo1818.com/live-api/v1_1/ranking-list/reward-out'
            res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
            Id_list = []
            for id in res['result']['resultList']:
                Id_list.append(id['streamerId'])
            Id_lists.append(Id_list)
    return Id_lists


def get_analyse():
    idss = get_one()
    for ids in idss:
        for id in ids:
            params1 = {
                'streamerId': '%s' % id,
                'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-7)).strftime('%Y-%m-%d')),
                'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
                'liveCategoryName': '',
            }
            url2 = 'http://www.huo1818.com/live-api/v1_2_1/streamer/goods-range-trend'
            res2 = json.loads(requests.get(url2, headers=get_headers(), params=params1).text)

            count_list2 = []
            for sum_temp2 in res2['result']:
                count_list2.append(sum_temp2['goodsNum'])
            count_temp2 = sum(count_list2)

            for temp4 in res2['result']:
                count_trend = {}
                count_trend['userid'] = id
                count_trend['count_range'] = str(temp4['leftRange']) + '-' + str(
                    temp4['rightRange'])
                count_trend['goods_num'] = temp4['goodsNum']
                if count_temp2 != 0:
                    count_trend['goods_rate'] = round((temp4['goodsNum'] / count_temp2) * 100, 2)
                else:
                    count_trend['goods_rate'] = 0.00
                count_trend['sell_count'] = temp4['sellCount']
                count_trend['sell_amount'] = temp4['sellAmount']
                print(count_trend)

                sql4 = "INSERT INTO t_from_user_count_trend (userid, count_range, goods_num, goods_rate, sell_count, sell_amount) VALUE ('%s','%s','%s','%s','%s','%s')"
                base4 = (
                    count_trend['userid'], count_trend['count_range'], count_trend['goods_num'], count_trend['goods_rate'], count_trend['sell_count'],
                    count_trend['sell_amount'])

                conn = pymysql.connect(host="111.231.0.33", port=3306, user="ceshi", password="ChaxunNewOtMySql1129",
                                       database="test",
                                       charset="utf8mb4")

                try:
                    cursor = conn.cursor()
                    cursor.execute(sql4 % base4)
                    conn.commit()
                except:
                    conn.ping()
                    cursor = conn.cursor()
                    cursor.execute(sql4 % base4)
                    conn.commit()
                    conn.rollback()
                conn.close()
            time.sleep(1)
# get_analyse()
