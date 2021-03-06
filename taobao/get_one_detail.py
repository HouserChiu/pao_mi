# coding: utf-8
import time

import requests
import urllib3
import re
import json
from headers_lists import get_headers1, get_headers2, get_headers3, get_headers4
from lxml import etree
from params_list import get_params1
from mongo_tb import mongo_info_taobao

# 请求大类得到一级页面的url
def one_product_detail(good_id):
    # 请求详情页面获取商品详细信息
    url1 = "https://item.taobao.com/item.htm?spm=a219r.lm874.14.1.45cb36a7Nv5owE&id={}&ns=1&abbucket=12".format(good_id)
    print(url1)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res1 = requests.get(url1, headers=get_headers3(), verify=False).text
    product_info = {}
    # 商品标题
    if etree.HTML(res1).xpath("//h3[@class='tb-main-title']/text()") != []:
        product_info['title'] = ''.join(etree.HTML(res1).xpath("//h3[@class='tb-main-title']/text()")).strip()
    else:
        product_info['title'] = ''.join(etree.HTML(res1).xpath("//meta[@name='keywords']/@content")).strip()
    # 店铺名称
    if etree.HTML(res1).xpath("//div[@class='tb-shop-name']/dl/dd/strong/a/@title") != []:
        product_info['shop_name'] = ''.join(etree.HTML(res1).xpath("//div[@class='tb-shop-name']/dl/dd/strong/a/@title")).strip()
    else:
        product_info['shop_name'] = ''.join(etree.HTML(res1).xpath('//a[@class="slogo-shopname"]/strong/text()'))
    product_info['goods_id'] = good_id
    product_info['source'] = url1
    # 商品图
    if etree.HTML(res1).xpath("//ul[@class='tb-thumb tm-clear']/li/a/img/@src") != []:
        product_info['imgsSrc'] = etree.HTML(res1).xpath("//ul[@class='tb-thumb tm-clear']/li/a/img/@src")
    else:
        product_info['imgsSrc'] = eval('[' + re.search('auctionImages.*?\[(.*?)\]', res1, re.S).group(1) + ']')
    # 判断商品视频是否存在
    temp_result = re.search('imgVedioID.*?\"(\d+)\"', res1, re.S)
    if temp_result != None:
        imgVedioID = temp_result.group(1)
        sellerId = re.search('sellerId.*?(\d+)', res1, re.S).group(1)
        product_info['videoUrl'] = "https://cloud.video.taobao.com/play/u/{}/p/1/e/6/t/1/{}.mp4".format(sellerId, imgVedioID)

    # 运费
    url2 = "https://mdskip.taobao.com/core/initItemDetail.htm"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res2 = requests.get(url2, headers=get_headers4(url1), params=get_params1(good_id), verify=False).text
    res_temp = '{' + re.search('defaultModel.*?\{(.*?)isSuccess', res2, re.S).group(1).rstrip('"').strip().rstrip(',')
    res_eve = json.loads(res_temp)
    if res_eve['deliveryDO']['deliverySkuMap']['default'][0]['postageFree'] == False:
        postage = float(res_eve['deliveryDO']['deliverySkuMap']['default'][0]['postage'].split(':')[1])
    else:
        postage = float(res_eve['deliveryDO']['deliverySkuMap']['default'][0]['money'])
    # 产品最终价格，最高价+运费
    if re.search('defaultItemPrice\".*?\"(.*?)\"', res1, re.S) != None:
        if '-' in re.search('defaultItemPrice\".*?\"(.*?)\"', res1, re.S).group(1):
            base_price = float(re.search('defaultItemPrice\".*?\"(.*?)\"', res1, re.S).group(1).split('-')[1].strip())
        else:
            base_price = float(re.search('defaultItemPrice\".*?\"(.*?)\"', res1, re.S).group(1).strip())
    else:
        if '-' in ''.join(etree.HTML(res1).xpath("//em[@class='tb-rmb-num']/text()")):
            base_price = float(''.join(etree.HTML(res1).xpath("//em[@class='tb-rmb-num']/text()")).split('-')[1].strip())
        else:
            base_price_temp = ''.join(etree.HTML(res1).xpath("//em[@class='tb-rmb-num']/text()"))
            base_price = float(base_price_temp)
    product_info['price'] = base_price + postage

    try:

        # 规格
        if etree.HTML(res1).xpath("//div[@class='tb-skin']/dl/dd/ul/li/a/span/text()") == []:
            key = etree.HTML(res1).xpath("//div[@class='tb-skin']/div/dl/dd/ul/li/a/span/text()")
        else:
            key = etree.HTML(res1).xpath("//div[@class='tb-skin']/dl/dd/ul/li/a/span/text()") == []
        if etree.HTML(res1).xpath("//div[@class='tb-skin']/dl/dd/ul/li/@data-value") == []:
            value = etree.HTML(res1).xpath("//div[@class='tb-skin']/div/dl/dd/ul/li/@data-value")
        else:
            value = etree.HTML(res1).xpath("//div[@class='tb-skin']/dl/dd/ul/li/@data-value")

        # 代号对应的规格名
        result_dict = {}
        for name, mark in zip(key, value):
            result_dict['%s' % mark.split(':')[1]] = name

        # 规格解析方法不同
        if re.search('skuMap.*?\{(.*?)propertyMemoMap', res1, re.S) != None:
            skumap = '{' + re.search('skuMap.*?\{(.*?)propertyMemoMap', res1, re.S).group(1).strip().rstrip(',')
            skuMap = json.loads(skumap)
        else:
            skumap = '{' + re.search('skuMap.*?\{(.*?)salesProp', res1, re.S).group(1).rstrip('"').strip().rstrip(',')
            skuMap = json.loads(skumap)

        new_dict = {}
        for k, v in skuMap.items():
            kk = re.findall('\:(\d+)\;', k, re.S)
            new_dict['%s' % kk] = v['price']

        # 图片链接
        temp_result = etree.HTML(res1).xpath("//ul[contains(@class,'J_TSaleProp tb-img')]/li/a/@style")
        if temp_result != []:
            color = etree.HTML(res1).xpath("//ul[contains(@class,'J_TSaleProp tb-img')]/li/a/span/text()")
            color_dict = {}
            for key1, value1 in zip(temp_result, color):
                color_dict['%s' % value1] = 'https:' + re.search('\((.*?)\)', key1, re.S).group(1)

            another_dict = {}
            for key4, value4 in new_dict.items():
                key2 = eval(key4)
                rep = [result_dict[x] if x in result_dict else x for x in key2]
                another_dict['%s' % rep] = {"price": value4, "url": ''}

            other_dict = {}
            for key3, value3 in another_dict.items():
                key7 = eval(key3)
                for y in key7:
                    if y in color_dict:
                        other_dict['%s' % key3] = {'price': '%s' % value3['price'], 'url': '%s' % color_dict[y]}

        else:
            other_dict = {}
            for key5, value5 in new_dict.items():
                key6 = eval(key5)
                rep = [result_dict[x] if x in result_dict else x for x in key6]
                other_dict['%s' % rep] = {"price": value5, "url": ''}
        product_info['spcification'] = other_dict
    except TypeError:
        pass
    # print(product_info)
    return product_info
















