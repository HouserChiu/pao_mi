'''
行业榜信息
'''
import requests
import json
import time
from mongo_xg import mongo_info_xg


def get_headers():
    headers = {
        'Host': 'mdataapi.xiguaji.com',
        'Connection': 'keep-alive',
        'sessionid': 'b066636a2360439eb8e5138660ae18cd',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36 MicroMessenger/7.0.13.1640(0x27000D34) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64 WeChat/arm32',
        'charset': 'utf-8',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wx0de4b2e1f3c239b7/4/page-frame.html',
    }
    return headers


def get_id():
    url = 'https://mdataapi.xiguaji.com/v1/Rank/GetIndusAreaInfos'
    params = {
        '_': '%s' % int(round(time.time() * 1000)),
    }
    res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
    Ids = res['Data']['IndustryInfos']
    Id_list = []
    for Id_info in Ids:
        Id_list.append(Id_info['Id'])
        if Id_info['ChildIndustryInfos']:
            for id2 in Id_info['ChildIndustryInfos']:
                Id_list.append(id2['Id'])
    return Id_list


def get_params():
    params_list = get_id()
    BizId_lists = []
    BizIdKey_lists = []
    for params_temp in params_list:
        params = {
            'period': '1',
            'rankType': '1',
            'pageIndex': '1',
            'pageSize': '30',
            'tidOne': '%s' % params_temp,
            '_': '%s' % int(round(time.time() * 1000)),
        }
        url = 'https://mdataapi.xiguaji.com/v1/Rank/GetRankInfos'
        res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
        ranklists = res['Data']['RankList']
        BizId_list = []
        BizIdKey_list = []
        for ranklist in ranklists:
            BizId = ranklist['BizId']
            BizIdKey = ranklist['BizId']
            BizId_list.append(BizId)
            BizIdKey_list.append(BizIdKey)
        BizId_lists.append(BizId_list)
        BizIdKey_lists.append(BizIdKey_list)
    return BizId_lists, BizIdKey_lists


def get_detail():
    BizId_listss = get_params()[0]
    BizIdKey_listss = get_params()[1]
    for BizId_lists, BizIdKey_lists in zip(BizId_listss, BizIdKey_listss):
        for BizId_list, BizIdKey_list in zip(BizId_lists, BizIdKey_lists):
            url = 'https://mdataapi.xiguaji.com/v1/MBizInfo/GetDetail'
            params = {
                'bizId': '%s' % BizId_list,
                'bizIdKey': '%s' % BizIdKey_list,
                '_': '%s' % int(round(time.time() * 1000)),
            }
            res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
            uer_info = {}
            # 平均阅读一篇数
            uer_info['FirstAvgRead'] = res['Data']['FirstAvgRead']
            # 平均阅读两篇数
            uer_info['SecondAvgRead'] = res['Data']['SecondAvgRead']

            # 平均阅读三篇或以上
            uer_info['ThirdMoreAvgRead'] = res['Data']['ThirdMoreAvgRead']
            # 发文数
            uer_info['RecentWeekArticlesCount'] = res['Data']['RecentWeekArticlesCount']
            # 平均点赞
            uer_info['FirstAvgLike'] = res['Data']['FirstAvgLike']
            # 平均留言
            uer_info['FirstAvgComment'] = res['Data']['FirstAvgComment']
            # 名称
            uer_info['BizName'] = res['Data']['BizName']
            # 西瓜指数
            uer_info['GuaZhiShu'] = res['Data']['GuaZhiShu']
            # 注册时间
            uer_info['RegisterPeriod'] = res['Data']['RegisterPeriod']
            # 公众号id
            uer_info['WechatId'] = res['Data']['WechatId']
            # 公众号简介
            uer_info['Desc'] = res['Data']['Desc']
            # 粉丝数
            uer_info['Fans'] = res['Data']['Fans']
            # 头像
            uer_info['Logo'] = res['Data']['Logo'].replace('/', '')
            # 统计周期
            uer_info['StatisticsPeriod'] = res['Data']['StatisticsPeriod']
            # 数据更新时间
            uer_info['UpdateTime'] = res['Data']['UpdateTime']
            # 博主更新时间
            uer_info['DataUpdateTime'] = res['Data']['DataUpdateTime']
            print(uer_info)
            mongo_info_xg.insert_item(uer_info)


get_detail()
