# coding: utf-8
import json
import re
import time
from headers_lists import get_headers3, get_headers2, get_headers7, get_headers9, get_headers4, get_headers10, get_headers11
from params_lists import get_params3, get_params4
import requests
import urllib3
from lxml import etree


def get_id_info(cate, i):
    params2 = {'beginpage': '%s' % i, 'asyncreq': '1', 'keywords': '%s' % cate, 'sortType': '', 'descendOrder': '',
         'province': '', 'city': '', 'priceStart': '', 'priceEnd': '', 'dis': '',
         'spm': 'a2609.11209760.it2i6j8a.30.44292de113BNUL', 'cosite': 'baidujj_pz', 'trackid': '{trackid}',
         'location': 're', 'pageid': '17145fa7ralgjD', 'p4pid': 'f5abf68bdcb94f5dab3c43c91ea6af09',
         'callback': 'jsonp_{}_51591'.format(int(round(time.time() * 1000))),
         '_': '%s' % int(round(time.time() * 1000)), }
    headers_eve = get_headers2(cate)
    url = 'https://data.p4psearch.1688.com/data/ajax/get_premium_offer_list.json'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=headers_eve, params=params2, verify=False).text
    res_temp = '{"data' + re.search('data(.*?)ret', res, re.S).group(1).rstrip('"').rstrip(',') + '}'
    res_eve = json.loads(res_temp)
    if res_eve["data"] != {}:
        temp = re.findall(r'\"eurl\":\"(.*?)\"', res, re.S)
        goods_id_list = []
        for eve in temp:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            print(eve)
            res = requests.get(eve, headers=get_headers3(), verify=False).text
            goods_id = re.search('<meta.*?b2c_auction.*?content=\"(\d+)\".*?>', res, re.S).group(1)
            print(goods_id)
            goods_id_list.append(goods_id)
        return goods_id_list
