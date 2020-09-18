#todo:
# coding=utf-8
# Author: tester_pei
import os

# 数据库配置
mysql_config = {
    'host': '111.231.0.33',
    'user': 'ceshi',
    'password': 'ChaxunNewOtMySql1129',
    'db': 'test'
}

# 代理
proxies = {"https": "http://127.0.0.1:8888"}

# 路径
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
RESPONSE_PATH = os.path.join(ROOT_PATH, 'response_online.json')

