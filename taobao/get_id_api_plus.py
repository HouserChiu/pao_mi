# coding: utf-8
import time

import requests
import urllib3
import re
import json
from headers_lists import get_headers1, get_headers2, get_headers3, get_headers4
from lxml import etree
from params_list import get_params1, get_params2
from mongo_tb import mongo_info_taobao

# 请求大类得到一级页面的url
def one_id_plus(pre_cate, i):
    url = "https://s.taobao.com/search"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=get_headers2(), params=get_params2(pre_cate, i), verify=False).text
    temp = eval('[' + re.search('allNids.*?\[(.*?)\]', res, re.S).group(1) + ']')
    product_id_list = []
    for good_id in temp:
        product_id_list.append(good_id)
    return product_id_list

