# coding:utf-8

import requests
import json
import datetime
import time
import pymysql


class LdlSpider():
    def __init__(self):
        self.url = 'http://www.huo1818.com/live-api/selector/tags'
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=utf-8',
            'Cookie': 'gr_user_id=3bb57c6b-679d-454c-9c06-2683109e4889; grwng_uid=95502437-1e8d-40ac-9116-e3f492e799c8; __51cke__=; Hm_lvt_a135ef5290d5317a9a4a051b9fee8f92=1592961783,1592990248; 8e22d1b16f393571_gr_session_id=56886d0d-1143-47cc-8194-8a03d46c7b93; 8e22d1b16f393571_gr_session_id_56886d0d-1143-47cc-8194-8a03d46c7b93=true; __tins__20450359=%7B%22sid%22%3A%201592994485675%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201592996288265%7D; __51laig__=4; Hm_lpvt_a135ef5290d5317a9a4a051b9fee8f92=1592994488; JSESSIONID=196CF4469BED6BB3344955D20B8E5777',
            'Host': 'www.huo1818.com',
            'PC_OPEN_ID': 'oQ4u90RuKb2NK12-lHlx67b42pEg',
            'Referer': 'http://www.huo1818.com/ranking/goods',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        }

    def GetCate(self):
        res = json.loads(requests.get(self.url, headers=self.headers).text)
        cate_list = []
        for cate in res['result']:
            cate_list.append(cate['tag'])
        # print(cate_list)
        return cate_list

    def GetParams(self):
        cates = self.GetCate()
        cate_list = []
        for cate in cates:
            params = [
                {'tag': '%s' % cate, 'type': '4', 'granularity': '1',
                 'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
                 'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
                 'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },
                {'tag': '%s' % cate, 'type': '5', 'granularity': '1',
                 'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
                 'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
                 'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },
            ]
            cate_list.append(params)
        print(cate_list)
        return cate_list

    def main(self):
        self.GetParams()


# if __name__ == '__main__':
#     ldl_spider = LdlSpider()
#     ldl_spider.main()

