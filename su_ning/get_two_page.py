# coding: utf-8

import json
import requests
import pprint
from headers_list import get_headers1, get_headers2, get_headers3
import re
from params_list import get_params1, get_params2

def one_page(cate, page):
    url1 = "http://search.suning.com/emall/mobile/wap/clientSearch.jsonp"
    res_temp = requests.get(url1, params=get_params1(cate, page), headers=get_headers2()).text
    res_eve = '{' + re.search('\{(.*?)jlf_fold_onoff', res_temp, re.S).group(1).rstrip('"').rstrip(',') + '}'
    pprint.pprint(res_eve)
    res1 = json.loads(res_eve)
    for goods in res1['goods']:
        url2 = "https://m.suning.com/product/0000000000/{}.html".format(goods['partnumber'])
        res2 = requests.get(url2, params=get_params2(), headers=get_headers3())

one_page("手机", "1")