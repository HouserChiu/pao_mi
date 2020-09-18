# coding: utf-8
import json

import requests
from headers_list import get_headers1, get_headers3
import re
import pprint


def get_id_info(cate):
    url = 'https://dc.3.cn/category/get?&callback=getCategoryCallback'
    res = requests.get(url, headers=get_headers1()).text
    cate_temp = json.loads(re.search('\((.*?)\)', res, re.S).group(1))
    # pprint.pprint(cate_temp)
    cate_dict = {}
    for data_temp in cate_temp['data']:
        for data_eve in data_temp['s']:
            for temp in data_eve['s']:
                for data in temp['s']:
                    cate_name = re.search('\|(.*?)\|\|', data['n'], re.S).group(1)
                    cate_url = re.search('(.*?)\|', data['n'], re.S).group(1)
                    if '-' in cate_url:
                        cate_dict['%s' % cate_name] = 'https://list.jd.com/list.html?cat=' + cate_url.replace('-', ',')
                    else:
                        cate_dict['%s' % cate_name] = 'https://' + cate_url
    res1 = requests.get(cate_dict['%s' % cate], headers=get_headers3()).text
    ids = eval('[' + re.search("wids.*?\'(.*?)\'", res1, re.S).group(1) + ']')
    # pprint.pprint(ids)
    return ids

# get_id('KTV音响')
