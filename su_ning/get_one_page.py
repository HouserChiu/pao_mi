# coding: utf-8

import json
import requests
import pprint
from headers_list import get_headers1, get_headers2
import re
from params_list import get_params1

def one_page(cate, page):
    url = "http://search.suning.com/emall/mobile/wap/clientSearch.jsonp"
    res_temp = requests.get(url, params=get_params1(cate, page), headers=get_headers2()).text
    res_eve = '{' + re.search('\{(.*?)jlf_fold_onoff', res_temp, re.S).group(1).rstrip('"').rstrip(',') + '}'
    # pprint.pprint(res_eve)
    res = json.loads(res_eve)
    id_list = []
    for goods in res['goods']:
        id_list.append(goods['partnumber'])
        # pprint.pprint(goods['partnumber'])
    return id_list

# one_page("手机", "1")



