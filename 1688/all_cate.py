# coding: utf-8
import re
import time
import urllib3
import requests
from web_spider import get_cate
from headers_lists import get_headers6
from cate_mongo import mongo_info_cate

def params_eve(cate):
    params = {
        'spm': 'a2609.11209760.it2i6j8a.30.44292de11fzneF',
        'cosite': 'baidujj_pz',
        'keywords': '%s' % cate,
        'trackid': '{trackid}',
        'location': 're',
    }
    yield params

def cate_eve(params):
    url = 'https://p4psearch.1688.com/p4p114/p4psearch/offer.htm'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, params=params, headers=get_headers6(), verify=False).text
    cate_info = {}
    cate_info['temp'] = eval('[' + re.search('relativeWords.*?\[(.*?)\]', res, re.S).group(1) + ']')
    print(cate_info)
    mongo_info_cate.insert_item(cate_info)

# def main(cate):
#     params_list = params_eve(cate)
#     for params in params_list:
#         cate_eve(params)
#         time.sleep(1)
#
# if __name__ == '__main__':
#     cate_list = get_cate()
#     for cate in cate_list:
#         main(cate)
