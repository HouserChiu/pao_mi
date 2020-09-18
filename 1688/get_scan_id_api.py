# coding: utf-8
import json
import re
import time
from headers_lists import get_headers3, get_headers2, get_headers7, get_headers9, get_headers4, get_headers10, get_headers11
from params_lists import get_params3, get_params4
import requests
import urllib3
from lxml import etree


def get_params(cate, i):
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
        product_info_list = []
        for eve in temp:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            print(eve)
            res = requests.get(eve, headers=get_headers3(), verify=False).text
            goods_id = re.search('<meta.*?b2c_auction.*?content=\"(\d+)\".*?>', res, re.S).group(1)
            print(goods_id)
            url1 = 'https://detail.1688.com/offer/{}.html?sk=consign'.format(goods_id)
            print(url1)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res = requests.get(url1, headers=get_headers3(), verify=False).text
            product_info = {}
            product_info['title'] = ''.join(etree.HTML(res).xpath("//html[@lang='zh-CN']/head/title/text()"))
            product_info['shop_name'] = re.search('<meta.*?og:product:nick.*?name=(.*?);.*?>', res, re.S).group(1)
            product_info['goods_id'] = re.search('<meta.*?b2c_auction.*?content=\"(\d+)\".*?>', res, re.S).group(1)
            product_info['source'] = url1
            # 商品图，创建product_img文件夹并下载图片
            product_info['imgsSrc'] = re.findall('<li.*?tab-trigger.*?original\"\:\"(.*?)\"', res, re.S)
            # 视频页面,创建product_video文件夹并下载视频
            memberId = re.search('member_id.*?\"(.*?)\"', res, re.S).group(1)
            videoId = re.search('videoId.*?\"(\d+)\"', res, re.S).group(1)
            if videoId != '0':
                res2 = requests.get('https://apps.1688.com/event/app/videoInfo/getVideoById.htm',
                                    params=get_params3(videoId, memberId), headers=get_headers4(), verify=False).text
                product_info['videoUrl'] = re.search('address\"\:\"(.*?)\"', res2, re.S).group(1)

            try:
                try:
                    skuProps = '[' + re.search('skuProps.*?\[(.*?)skuMap', res, re.S).group(1).rstrip(
                        '"').strip().rstrip(
                        ',')
                    skuMap = '{' + re.search('skuMap.*?\{(.*?)end', res, re.S).group(1).rstrip('"').strip().rstrip(
                        ',').rstrip(
                        '}').strip().rstrip(',')
                    Specifications1 = json.loads(skuProps)
                    Specifications2 = json.loads(skuMap)

                except json.decoder.JSONDecodeError:
                    skuProps = '[' + re.search('skuProps.*?\[(.*?)skuMap', res, re.S).group(1).rstrip(
                        '"').strip().rstrip(
                        ',')
                    skuMap = '{' + re.search('skuMap.*?\{(.*?)end', res, re.S).group(1).strip().rstrip(',')
                    Specifications1 = json.loads(skuProps)
                    Specifications2 = json.loads(skuMap)

                base_price = re.search('consignBasePrice\"\:\"(.*?)\"', res, re.S).group(1)
                if '-' in base_price:
                    base_price_eve = base_price.split('-')[1]
                else:
                    base_price_eve = base_price

                # 运费页面
                url4 = 'https://laputa.1688.com/offer/ajax/widgetList.do'
                res4 = requests.get(url4, headers=get_headers9(product_info['goods_id']),
                                    params=get_params4(product_info['goods_id']),
                                    verify=False).text
                res_temp = '{"data' + re.search('data(.*?)message', res4, re.S).group(1).rstrip('"').rstrip(',') + '}'
                res_eve = json.loads(res_temp)
                if res_eve['data']['data']['offerdetail_ditto_postage']['showFreightCost'] == False:
                    fee = 10
                elif res_eve['data']['data']['offerdetail_ditto_postage']['freightCost'] == []:
                    fee = 0
                else:
                    fee = res_eve['data']['data']['offerdetail_ditto_postage']['freightCost'][0]['costItems'][0][
                        'value']
                # 产品最终价格，分销/代发价+运费
                product_info['price'] = float(base_price_eve) + float(fee)

                # 有规格图，无价格
                img_dict = {}
                for value_eve in Specifications1:
                    for vv_eve in value_eve['value']:
                        if "imageUrl" in vv_eve.keys():
                            img_dict["%s" % vv_eve["name"]] = {"price": "", "url": vv_eve['imageUrl']}
                # 有价格，无规格图
                price_dict = {}
                for k, v in Specifications2.items():
                    if "price" in v.keys():
                        price_dict[k.replace('gt;', '').replace("/", "").replace("*", "")] = {'price': v['price'],
                                                                                              'url': ''}
                    else:
                        price_dict[k.replace('gt;', '').replace("/", "").replace("*", "")] = {
                            'price': product_info['price'],
                            'url': ''}
                # 构建新的json，含有价格和规格图，存入新的文件中
                for key1, value1 in img_dict.items():
                    for key2, value2 in price_dict.items():
                        if key1 in key2:
                            price_dict['%s' % key2]['url'] = img_dict['%s' % key1]['url']

                product_info['spcification'] = price_dict
            except AttributeError:
                pass
            product_info_list.append(product_info)
        return product_info_list
