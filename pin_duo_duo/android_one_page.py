# -*- coding: utf-8 -*-
'''
安卓4.5.1
'''
import requests
import json
import urllib3
import pprint
from headers_list import get_headers2


def get_cate():
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
    # pprint.pprint(cate_dict)
    return cate_dict

# get_cate()
