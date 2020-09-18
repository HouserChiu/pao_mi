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

def get_detail(category, page):
    url = "http://api.yangkeduo.com/operations?pdduid=1393851438"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = json.loads(requests.get(url, headers=get_headers2(), verify=False).content.decode('utf-8'))
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
    res1 = json.loads(requests.get(url1, params=get_params1(page), headers=get_headers2(), verify=False).content.decode('utf-8'))
    product_info_list = []
    for goods_id in res1['goods_list']:
        idd = goods_id['goods_id']
        mall_id = goods_id['mall_id']
        url2 = "http://api.yangkeduo.com/api/oakstc/v14/goods/{}?goods_id={}&from=0&pdduid=1393851438".format(idd, idd)
        res2 = json.loads(requests.get(url2, headers=get_headers2(), verify=False).content.decode('utf-8'))
        product_info = {}
        product_info['title'] = res2['goods_name']
        product_info['goods_id'] = idd
        product_info['price'] = res2['market_price'] / 1000
        imgsSrc_list = []
        for video_img_temp in res2['gallery']:
            video_img_eve = video_img_temp['url']
            if '.mp4' in video_img_eve:
                product_info['videoUrl'] = video_img_eve
            else:
                Src = video_img_eve
                imgsSrc_list.append(Src)
        product_info['imgsSrc'] = imgsSrc_list
        product_info['source'] = "https://mobile.yangkeduo.com/goods2.html?goods_id={}".format(idd)
        url3 = "http://api.yangkeduo.com/mall/{}/info?check_merchant_coupon=no&pdduid=1393851438".format(mall_id)
        res3 = json.loads(requests.get(url3, headers=get_headers2()).text)
        product_info['shop_name'] = res3['mall_name']
        product_info_list.append(product_info)
        # pprint.pprint(product_info)
    return product_info_list

# get_cate("食品饮料-无辣不欢", "0")







