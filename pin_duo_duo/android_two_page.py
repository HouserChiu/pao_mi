# -*- coding: utf-8 -*-
'''
安卓4.5.1
'''
import requests
import json
import urllib3
import pprint
from headers_list import get_headers2
from params_list import get_params1

def get_id_info(category, page):
    url = "http://api.yangkeduo.com/operations?pdduid=1393851438"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = json.loads(requests.get(url, headers=get_headers2(), verify=False).text)
    cate_dict = {}
    for temp_child in res:
        for eve_child in temp_child['children']:
            cate_id = eve_child['id']
            if 'opt_desc' in eve_child:
                cate_name = eve_child['opt_desc']
            else:
                cate_name = eve_child['opt_name']
            cate_dict['%s' % cate_name] = cate_id
    url1 = "http://api.yangkeduo.com/v4/operation/{}/groups".format(cate_dict['%s' % category])
    res1 = json.loads(requests.get(url1, params=get_params1(page), headers=get_headers2(), verify=False).text)
    pprint.pprint(res1)
    idd_list = []
    for goods_id in res1['goods_list']:
        idd = goods_id['goods_id']
        idd_list.append(idd)
    return idd_list
