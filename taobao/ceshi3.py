# coding: utf-8
import json

import requests
import urllib3
from lxml import etree
from operator import itemgetter
from itertools import groupby
import re

def get_detail():
    url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.27.5a9e2b71hb2OPd&id=621848137263&ns=1&abbucket=3&skuId=4408722940965"
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'thw=cn; cookie2=11baad53f0e72b068205987923f6a275; t=2860081a67b697359e9c35a3d908fa6f; _tb_token_=ee8d7fe63eee3; cna=8FmVF+VBJxgCAd7RUm5VHyu7; _samesite_flag_=true; v=0; sgcookie=EAmJODYSalo2D38S44REt; uc3=vt3=F8dBxGPjYkLSvJHtcQg%3D&id2=UoH7LXuyKB0VPQ%3D%3D&lg2=UtASsssmOIJ0bQ%3D%3D&nk2=F5RHpr11toKZszuTPfk%3D; csg=131989df; lgc=tb2718229_2012; dnk=tb2718229_2012; skt=6dabb9036b7d770a; existShop=MTU5NTIwOTA4MA%3D%3D; uc4=id4=0%40UOnkSQ%2Fs2F54PslpQqrfo59Z8n0v&nk4=0%40FY4MtLzu6TOXXT69SO8b0hhFA47t79rzoQ%3D%3D; tracknick=tb2718229_2012; _cc_=URm48syIZQ%3D%3D; enc=CYSg0CkEut0iBtryO6OkfuTPQqsgw6kBg6bqNR%2Fe7hoBnAPKw0OnvQdfRmDG0XC2ZeBjbya34%2By%2F%2FtaJ0vR%2BgA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=0_1; _m_h5_tk=2c453fb7a647f66cc16d76dbac6ec6ec_1595223610616; _m_h5_tk_enc=88a1c2ec63047a84588a773e0b1076a8; tfstk=cDYNBHqdjV3N2y_j2N_45qEvDCQOCXRMiy55j3BkwVgsOur22C5cJ-CnO-CFGPkdj; UM_distinctid=1736ae7e2e88a3-07cd2343c47ad3-b7a1334-1fa400-1736ae7e2e9627; uc1=cookie21=VT5L2FSpccLuJBreK%2BBd&cookie14=UoTV6e9oUSSitQ%3D%3D&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&existShop=false&pas=0; l=eBTnmTKrOLp9X7sDpOfwnurza77tIIRAguPzaNbMiOCPO_5e5wBhWZk7C38wCnGVh6kwR3oIr-vXBeYBqoYwsWRKe5DDwQDmn; isg=BJSUS_84t1LmaiOFCuWE7MfzZdIG7bjXqgsMpS51Lp-iGTRjVv_7ZtwbHRGB4fAv',
        'referer': 'https://s.taobao.com/search?spm=a21bo.2017.201867-links-3.53.275511d904BgZe&q=%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200420&ie=utf8',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=headers, verify=False).text
    # print(res)
    temp_result = etree.HTML(res).xpath("//ul[contains(@class,'J_TSaleProp tb-img')]/li/a/@style")
    # print(temp_result)
    if temp_result != []:
        color = etree.HTML(res).xpath("//ul[contains(@class,'J_TSaleProp tb-img')]/li/a/span/text()")
        color_dict = {}
        for key1, value1 in zip(temp_result, color):
            color_dict['%s' % value1] = 'https:' + re.search('\((.*?)\)', key1, re.S).group(1)
        print(color_dict)

    #
    # print(temp_result)
get_detail()
