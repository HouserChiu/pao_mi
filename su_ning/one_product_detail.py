# coding: utf-8

import json
import requests
import pprint
from headers_list import get_headers1, get_headers2, get_headers3, get_headers4, get_headers5
import re
from params_list import get_params1, get_params2
from lxml import etree
import urllib3


def one_detail(goods_id):
    url2 = "https://m.suning.com/product/0000000000/{}.html".format(goods_id)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res2 = requests.get(url2, params=get_params2(), headers=get_headers3(), verify=False).text
    # pprint.pprint(res2)
    product_info = {}
    product_info['title'] = ''.join(etree.HTML(res2).xpath("//span[@id='product-name']/text()"))
    product_info['goods_id'] = goods_id
    info_json = re.findall('shopName\:.*?\"(.*?)\"', res2, re.S)
    product_info['shop_name'] = info_json[1]
    product_info['source'] = "https:" + re.search('toPcUrl.*?\"(.*?)\"', res2, re.S).group(1).replace('\\u002F', '/')
    res3 = requests.get(product_info['source'], headers=get_headers4(), verify=False).text
    cluster = eval(
        '[' + re.search('clusterMap\"\:.*?\[(.*?)colorList', res3, re.S).group(1).rstrip('"').strip().rstrip(','))
    cluster_list = []
    zero_list = []
    for clu in cluster:
        for cl in clu['itemCuPartNumber']:
            cluster_list.append(cl['partNumber'])
            zero_list.append(cl['partNumber'][0:5] * 2)
    # 规格url构建
    url4_one = str(cluster_list).replace('[', '').replace("'", "").replace(']', '').replace(' ', '')
    url4_two = str(zero_list).replace('[', '').replace("'", "").replace(']', '').replace(' ', '')
    url4 = 'https://icps.suning.com/icps-web/getVarnishAllPriceNoCache/' + url4_one + '_028_0280199_' + url4_two + '_1_getClusterPrice.jsonp?callback=getClusterPrice'
    price_dict = {}
    res4_temp = requests.get(url4, headers=get_headers5(), verify=False).text
    res4_eve = re.search('\((.*?)\)', res4_temp, re.S).group(1)
    res4_evet = json.loads(res4_eve)
    for res4 in res4_evet:
        price_dict['%s' % res4['cmmdtyCode']] = res4['price']

    img_dict = {}
    for color in etree.HTML(res3).xpath("//dl[@id='colorItemList']/dd/ul/li"):
        url5 = 'https:' + ''.join(color.xpath("./a/@href"))
        res5 = requests.get(url5, headers=get_headers4(), verify=False).text
        imgs = json.loads(''.join(etree.HTML(res5).xpath("//script[@type='application/ld+json']/text()")))
        img_dict['%s' % ''.join(color.xpath("./@title"))] = imgs['images'][0]

    version_dict = {}
    for version in etree.HTML(res3).xpath("//dl[@id='versionItemList']/dd/ul/li"):
        version_dict['%s' % ''.join(version.xpath("./@sku"))] = ''.join(version.xpath("./@title"))

    merge_dict = {}
    for key1, value1 in version_dict.items():
        for key2, value2 in img_dict.items():
            merge_dict["%s" % value1 + '&' + key2] = {'url': '%s' % value2, 'id': '%s' % key1}

    merge_price = {}
    for key3, value3 in merge_dict.items():
        if value3['id'] in price_dict:
            merge_price['%s' % key3] = {'price': '%s' % price_dict['%s' % value3['id']], 'url': '%s' % value3['url']}
    product_info['spcification'] = merge_price

    price_list = []
    for key4, value4 in merge_price.items():
        price_list.append(float(value4['price']))
    product_info['price'] = min(price_list)

    video = re.search('videoUrl\"\:.*?\"(.*?)\"', res3, re.S)
    if video != None:
        product_info['videoUrl'] = re.search('videoUrl\"\:.*?\"(.*?)\"', res3, re.S).group(1)
    imgsSrc = etree.HTML(res2).xpath("//div[@class='swiper-slide']/img")
    imgsSrc_list = []
    for imgSrc in imgsSrc:
        imgsSrc_list.append("https:" + ''.join(imgSrc.xpath("./@src")))
    product_info['imgsSrc'] = imgsSrc_list
    # pprint.pprint(product_info)
    return product_info
# one_detail("11346312311")
