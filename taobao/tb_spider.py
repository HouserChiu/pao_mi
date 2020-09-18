# coding: utf-8

import requests
import urllib3
import re
import json
from headers_lists import get_headers1, get_headers2, get_headers3, get_headers4
from lxml import etree
from params_list import get_params1
from mongo_tb import mongo_info_taobao

# 请求大类得到一级页面的url
def cate_one():
    url = "https://tce.alicdn.com/api/data.htm?ids=222887%2C222890%2C222889%2C222886%2C222906%2C222898%2C222907%2C222885%2C222895%2C222878%2C222908%2C222879%2C222893%2C222896%2C222918%2C222917%2C222888%2C222902%2C222880%2C222913%2C222910%2C222882%2C222883%2C222921%2C222899%2C222905%2C222881%2C222911%2C222894%2C222920%2C222914%2C222877%2C222919%2C222915%2C222922%2C222884%2C222912%2C222892%2C222900%2C222923%2C222909%2C222897%2C222891%2C222903%2C222901%2C222904%2C222916%2C222924&callback=tbh_service_cat"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=get_headers1(), verify=False).text
    result = re.search('\((.*?)\)', res, re.S).group(1)
    temp = json.loads(result)
    for eve in temp.values():
        for item in eve['value']['list']:
            if len(item) == 3:
                cate_link_dict = {}
                cate_link_dict['name'] = item['name']
                cate_link_dict['link'] = item['link']
                # print(cate_link_dict)
                # print(cate_link_dict['name'])
                yield cate_link_dict['link']

# 请求一级页面获取商品id
def id_two(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=get_headers2(), verify=False).text
    temp = eval('[' + re.search('allNids.*?\[(.*?)\]', res, re.S).group(1) + ']')
    for good_id in temp:
        yield good_id

# 请求详情页面获取商品详细信息
def detail_three(good_id):
    url = "https://item.taobao.com/item.htm?spm=a219r.lm874.14.1.45cb36a7Nv5owE&id={}&ns=1&abbucket=12".format(good_id)
    res = requests.get(url, headers=get_headers3(), verify=False).text
    product_info = {}
    # 商品标题
    if etree.HTML(res).xpath("//h3[@class='tb-main-title']/text()") != []:
        product_info['title'] = ''.join(etree.HTML(res).xpath("//h3[@class='tb-main-title']/text()")).strip()
    else:
        product_info['title'] = ''.join(etree.HTML(res).xpath("//meta[@name='keywords']/@content")).strip()
    # 店铺名称
    if etree.HTML(res).xpath("//div[@class='tb-shop-name']/dl/dd/strong/a/@title") != []:
        product_info['shop_name'] = ''.join(etree.HTML(res).xpath("//div[@class='tb-shop-name']/dl/dd/strong/a/@title")).strip()
    else:
        product_info['shop_name'] = ''.join(etree.HTML(res).xpath('//a[@class="slogo-shopname"]/strong/text()'))
    product_info['goods_id'] = good_id
    product_info['source'] = url
    # 商品图
    if etree.HTML(res).xpath("//ul[@class='tb-thumb tm-clear']/li/a/img/@src") != []:
        product_info['imgsSrc'] = etree.HTML(res).xpath("//ul[@class='tb-thumb tm-clear']/li/a/img/@src")
    else:
        product_info['imgsSrc'] = eval('[' + re.search('auctionImages.*?\[(.*?)\]', res, re.S).group(1) + ']')
    # 判断商品视频是否存在
    temp_result = re.search('imgVedioID.*?\"(\d+)\"', res, re.S)
    if temp_result != None:
        imgVedioID = temp_result.group(1)
        sellerId = re.search('sellerId.*?(\d+)', res, re.S).group(1)
        product_info['videoUrl'] = "https://cloud.video.taobao.com/play/u/{}/p/1/e/6/t/1/{}.mp4".format(sellerId, imgVedioID)

    # 运费
    url1 = "https://mdskip.taobao.com/core/initItemDetail.htm"
    res1 = requests.get(url1, headers=get_headers4(url), params=get_params1(good_id)).text
    res_temp = '{' + re.search('defaultModel.*?\{(.*?)isSuccess', res1, re.S).group(1).rstrip('"').strip().rstrip(',')
    res_eve = json.loads(res_temp)
    if res_eve['deliveryDO']['deliverySkuMap']['default'][0]['postageFree'] == False:
        postage = float(res_eve['deliveryDO']['deliverySkuMap']['default'][0]['postage'].split(':')[1])
    else:
        postage = float(res_eve['deliveryDO']['deliverySkuMap']['default'][0]['money'])
    # 产品最终价格，最高价+运费
    try:
        base_price = float(re.search('defaultItemPrice.*?\"(.*?)\"', res, re.S).group(1).split('-')[1].strip())
    except:
        base_price = float(''.join(etree.HTML(res).xpath("//em[@class='tb-rmb-num']/text()")))
    product_info['price'] = base_price + postage

    # 规格
    if etree.HTML(res).xpath("//div[@class='tb-skin']/dl/dd/ul/li/a/span/text()") == []:
        key = etree.HTML(res).xpath("//div[@class='tb-skin']/div/dl/dd/ul/li/a/span/text()")
    else:
        key = etree.HTML(res).xpath("//div[@class='tb-skin']/dl/dd/ul/li/a/span/text()") == []
    if etree.HTML(res).xpath("//div[@class='tb-skin']/dl/dd/ul/li/@data-value") == []:
        value = etree.HTML(res).xpath("//div[@class='tb-skin']/div/dl/dd/ul/li/@data-value")
    else:
        value = etree.HTML(res).xpath("//div[@class='tb-skin']/dl/dd/ul/li/@data-value")

    # 代号对应的规格名
    result_dict = {}
    for name, mark in zip(key, value):
        result_dict['%s' % mark.split(':')[1]] = name

    # 规格解析方法不同
    try:
        skumap = '{' + re.search('skuMap.*?\{(.*?)propertyMemoMap', res, re.S).group(1).strip().rstrip(',')
        skuMap = json.loads(skumap)
    except:
        skumap = '{' + re.search('skuMap.*?\{(.*?)salesProp', res, re.S).group(1).rstrip('"').strip().rstrip(',')
        skuMap = json.loads(skumap)

    new_dict = {}
    for k, v in skuMap.items():
        kk = re.findall('\:(\d+)\;', k, re.S)
        new_dict['%s' % kk] = v['price']

    # 图片链接
    temp_result = etree.HTML(res).xpath("//ul[contains(@class,'J_TSaleProp tb-img')]/li/a/@style")
    if temp_result != []:
        color = etree.HTML(res).xpath("//ul[contains(@class,'J_TSaleProp tb-img')]/li/a/span/text()")
        color_dict = {}
        for key1, value1 in zip(temp_result, color):
            color_dict['%s' % value1] = 'https:' + re.search('\((.*?)\)', key1, re.S).group(1)

        another_dict = {}
        for key, value in new_dict.items():
            key2 = eval(key)
            rep = [result_dict[x] if x in result_dict else x for x in key2]
            another_dict['%s' % rep] = {"price": value, "url": ''}

        other_dict = {}
        for key3, value3 in another_dict.items():
            key4 = eval(key3)
            for y in key4:
                if y in color_dict:
                    other_dict['%s' % key3] = {'price': '%s' % value3['price'], 'url': '%s' % color_dict[y]}

    else:
        other_dict = {}
        for key, value in new_dict.items():
            key2 = eval(key)
            rep = [result_dict[x] if x in result_dict else x for x in key2]
            other_dict['%s' % rep] = {"price": value, "url": ''}
    product_info['spcification'] = other_dict

    return product_info












