# todo:
# coding=utf-8
# Author: tester_pei

import datetime
import requests
from db.sql import sql_001, sql_003, sql_004, sql_005
import json


def get_user_info(userid, headers, **kwargs):
    '''
    66榜基本信息获取
    :param userid: 66榜userid -->通过分类列表获取userid-->get_user_list_info(get_userid)
    :param headers: 带上cookie和token的头部
    :param kwargs: 调试时可以传入proxies——抓包代理
    :return: dict
    '''
    user_detail_url = 'https://66bang.com/home/api/v1/rank/guys/' + userid
    # user_info = requests.get(url=user_detail_url, headers=headers, proxies=proxies, verify=False) # 调试
    r = requests.get(url=user_detail_url, headers=headers).text
    user_info = json.loads(r)
    print(user_info)

    # user_info = r.json()
    t_from_user_info = {}
    # 数据来源： 66榜网站==1
    t_from_user_info['platform'] = '1'
    # 自媒体账号
    t_from_user_info['account'] = user_info['unique_id']
    # 自媒体昵称
    t_from_user_info['name'] = user_info['nickname']
    # 自媒体头像
    t_from_user_info['head_thumb'] = user_info['avatar_medium_url']
    # 判断男女
    if user_info['gender'] == 1:
        t_from_user_info['sex'] = '男'
    else:
        t_from_user_info['sex'] = '女'
    t_from_user_info['stars'] = ''
    # 计算年龄
    if user_info['birthday'] != '':
        now_year = datetime.datetime.today().year
        birthday = datetime.datetime.strptime(user_info['birthday'], '%Y-%m-%d').year
        age = now_year - birthday
        t_from_user_info['age'] = age
    else:
        t_from_user_info['age'] = ''
    # 地区 district
    t_from_user_info['district'] = user_info['city']
    # 自媒体简介
    t_from_user_info['remark'] = user_info['signature']
    # 自媒体标签
    t_from_user_info['label'] = user_info['cate']
    # mcn
    t_from_user_info['mcn'] = user_info['mcn_info']
    # 粉丝数
    t_from_user_info['fans'] = user_info['follower_count']
    # 作品数
    t_from_user_info['collection'] = user_info['aweme_count']
    # 点赞数
    t_from_user_info['likes'] = user_info['total_favorited']
    # url
    t_from_user_info['url'] = user_detail_url
    # 通过分类查询id
    if 'cate' in user_info.values():
        categoryid = sql_001(user_info['cate'])
        t_from_user_info['categoryid'] = categoryid
    else:
        t_from_user_info['categoryid'] = user_info['cate']
    return t_from_user_info


def get_user_list_info(kind, headers, save, get='id', page=1, pageSize=20, dateType='day', **kwargs):
    '''
    获取66榜用户id
    :param kind: 分类-->66榜分类-->get_66bang_kind
    :param headers:带上cookie和token的头部
    :param get:默认id，传入info获取列表数据（数据不如详情）
    :param page:默认1，待开通vip后可解锁
    :param pageSize:默认20，待开通vip后可解锁
    :param dateType:默认day-日榜，week-周榜，month-月榜
    :param kwargs:试时可以传入proxies——抓包代理
    :return:id-->list;info-->dict
    '''

    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    url = 'https://66bang.com/home/api/v1/rank/follower_goup/' + year + '/0' + month + '/0' + day + '/'
    data = {'cate_name': kind,
            'page': page,
            'pageSize': pageSize,
            'dateType': dateType
            }
    # response = requests.get(url=url, params=data, headers=headers, proxies=proxies, verify=False) # 调试
    response = requests.get(url=url, params=data, headers=headers)
    user_detail_list = response.json()['results']
    if get == 'id':
        userid_list = []
        for user_detail in user_detail_list:
            userid_list.append(user_detail['userid'])
        return userid_list
    elif get == 'info':
        t_from_user_info = {}
        for user_detail in user_detail_list:
            user_info = {}
            t_from_user_info[user_detail['nickname']] = user_info
            # 数据来源： 66榜网站==1
            user_info['platform'] = '1'
            user_info['name'] = user_detail['nickname']
            user_info['url'] = 'https://66bang.com/home/api/v1/rank/guys/' + user_detail['userid']
            user_info['fans'] = user_detail['total_favorited']
            user_info['collection'] = user_detail['aweme_count']
            user_info['likes'] = user_detail['total_favorited']
            user_info['head_thumb'] = user_detail['avatar_medium_url']
            user_info['label'] = user_detail['cate']
            # 通过分类查询id
            if 'cate' in user_detail.values():
                categoryid = sql_001(user_detail['cate'])
                user_info['categoryid'] = categoryid
            else:
                user_info['categoryid'] = 1000
            # 通过URL识别是否已收录
            # 判断查询结果是否为空
            # if sql_004(user_info['url']) == '':
            #     if save == True:
            #         sql_003(user_info)
            # elif sql_004(user_info['url']) != '':
            #     sql_url = sql_004(user_info['url'])
            #     if sql_url == user_info['url']:
            #         # 如果URL已收录则执行更新操作
            #         sql_005(dict=user_info)
            # else:
            #     print('请注意，现在的数据未保存')
        return t_from_user_info


def get_66bang_kind(headers):
    '''
    获取66榜的所有分类
    :param headers: 带上cookie和token的头部
    :return: list
    '''
    url = 'https://66bang.com/home/api/v1/rank/category/get/'
    response = requests.get(url=url, headers=headers)
    results_list = response.json()['results']
    kind_list = []
    for kind in results_list:
        kind_list.append(kind['name'])
    return kind_list