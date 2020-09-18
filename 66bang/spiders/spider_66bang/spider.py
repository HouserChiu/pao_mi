# todo:
# coding=utf-8
# Author: tester_pei
import datetime
import requests

from common.url_data import get_66bang_headers
from db.sql import sql_002
from spiders.spider_66bang.method import get_66bang_kind
from spiders.spider_66bang.method import get_user_list_info
from spiders.spider_66bang.method import get_user_info

# 配置
# Authorization = 'Token 845bb047b41d84bd130e19daeb15695a2208a768'
Authorization = 'Token 7cdb464b6ef23abcd55c8353ac5e7bf60be365e0'
SESSIONID = 'session_id_fcda5cf6d95f553699008061a8d79924'
# SESSIONID = 'session_id_eb1178525b0655a18fbe4cfb30484c32'
headers = get_66bang_headers(Authorization, SESSIONID)

# 获取所有分类
kind_list = get_66bang_kind(headers)
# 获取所有分类下的网红id,每一种分类下有默认的20条网红信息,未开通vip时仅获取默认的20条部分数据
for kind in kind_list:
    # 仅获取id(列表)
    id_list = get_user_list_info(kind, headers, save=True, get='id')
    # 遍历所有id进入详情页抓取更多数据
    for i in id_list:
        t_from_user_info = get_user_info(userid=i, headers=headers)
        print(t_from_user_info)
        # 将获取的数据存入数据库
        sql_002(t_from_user_info)
    # 仅获取列表用户数据(字典)
    # user_info_dict = get_user_list_info(kind, headers, save=True, get='info')
