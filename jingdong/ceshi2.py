# coding: utf-8

import requests
from headers_list import get_headers3, get_headers4
from lxml import etree
import re
from params_list import get_params2, get_params3
import pprint

url = "https://item.jd.com/70108536727.html"
res = requests.get(url, headers=get_headers3()).text
product_info = {}
product_info['title'] = ''.join(etree.HTML(res).xpath("//html[@lang='zh-CN']/head/title/text()"))
lis = etree.HTML(res).xpath("//ul[@class='lh']/li")
imgsSrc_list = []
for li in lis:
    imgsSrc = "https:" + ''.join(li.xpath("./img/@src"))
    imgsSrc_list.append(imgsSrc)
product_info['imgsSrc'] = imgsSrc_list
product_info['shop_name'] = ''.join(etree.HTML(res).xpath("//div[@class='J-hove-wrap EDropdown fr']/div/div/a/@title"))
# 获取视频id
if re.search('mainVideoId\"\:.*?\"(\d+)\"', res, re.S) != None:
    mainVideoId = re.search('mainVideoId\"\:.*?\"(\d+)\"', res, re.S).group(1)
    url1 = "https://c.3.cn/tencent/video_v3"
    res1 = requests.get(url1, params=get_params2(mainVideoId), headers=get_headers4(url)).text
    product_info['videoUrl'] = re.search('playUrl\"\:.*?\"(.*?)\"', res1, re.S).group(1)
# 获取价格请求参数中的venderId
venderId = re.search('venderId\:.*?(\d+)', res, re.S).group(1)
url2 = "https://c0.3.cn/stock"
goods_id = '70108536727'
cat = re.search('cat\:.*?\[(.*?)\]', res, re.S).group(1)
res2 = requests.get(url2, headers=get_headers4(url), params=get_params3(goods_id, venderId, cat)).text
product_info['price'] = re.search('\"p\"\:.*?\"(.*?)\"', res2, re.S).group(1)
# 获取商品的所有规格id
color_dict = {}
for color in etree.HTML(res).xpath("//div[@id='choose-attr-1']/div[@class='dd']/div"):
    # 颜色名
    key = ''.join(color.xpath("./@data-value"))
    # 颜色对应图片的链接为字典值
    color_dict['%s' % key] = 'https:' + ''.join(color.xpath("./a/img/@src"))
# pprint.pprint(color_dict)

sku_list = eval('[' + re.search('colorSize.*?\[(.*?)\]', res, re.S).group(1) + ']')
sku_dict = {}
for sku in sku_list:
    res3 = requests.get(url2, headers=get_headers4(url), params=get_params3(sku['skuId'], venderId, cat)).text
    price = re.search('\"p\"\:.*?\"(.*?)\"', res3, re.S).group(1)
    sku.pop('skuId')
    sku_dict['%s' % list(sku.values())] = price
# pprint.pprint(sku_dict)

another_dict = {}
for k, v in sku_dict.items():
    k1 = eval(k)
    for x in k1:
        if x in color_dict:
            another_dict['%s' % k] = {"price": v, 'url': '%s' % color_dict[x]}
pprint.pprint(another_dict)

