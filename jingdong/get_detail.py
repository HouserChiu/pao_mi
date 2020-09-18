# coding: utf-8
import json
import requests
from headers_list import get_headers3, get_headers4, get_headers1
from lxml import etree
import re
from params_list import get_params2, get_params3
import pprint


def get_detail_info(cate):
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
    product_info_list = []
    for ids_eve in ids:
        url4 = "https://item.jd.com/{}.html".format(ids_eve)
        print(url4)
        res4 = requests.get(url4, headers=get_headers3()).text
        product_info = {}
        product_info['source'] = url4
        product_info['goods_id'] = ids_eve
        product_info['title'] = ''.join(etree.HTML(res4).xpath("//html[@lang='zh-CN']/head/title/text()"))
        lis = etree.HTML(res4).xpath("//ul[@class='lh']/li")
        imgsSrc_list = []
        for li in lis:
            imgsSrc = "https:" + ''.join(li.xpath("./img/@src"))
            imgsSrc_list.append(imgsSrc)
        product_info['imgsSrc'] = imgsSrc_list
        product_info['shop_name'] = ''.join(
            etree.HTML(res4).xpath("//div[@class='J-hove-wrap EDropdown fr']/div/div/a/@title"))
        # 获取视频id
        if re.search('mainVideoId\"\:.*?\"(\d+)\"', res4, re.S) != None:
            mainVideoId = re.search('mainVideoId\"\:.*?\"(\d+)\"', res4, re.S).group(1)
            url1 = "https://c.3.cn/tencent/video_v3"
            res1 = requests.get(url1, params=get_params2(mainVideoId), headers=get_headers4(url4)).text
            product_info['videoUrl'] = re.search('playUrl\"\:.*?\"(.*?)\"', res1, re.S).group(1)
        # 获取价格请求参数中的venderId
        venderId = re.search('venderId\:.*?(\d+)', res4, re.S).group(1)
        url2 = "https://c0.3.cn/stock"
        cat = re.search('cat\:.*?\[(.*?)\]', res4, re.S).group(1)
        res2 = requests.get(url2, headers=get_headers4(url4), params=get_params3(ids_eve, venderId, cat)).text
        if re.search('\"p\"\:.*?\"(.*?)\"', res2, re.S) != None:
            product_info['price'] = re.search('\"p\"\:.*?\"(.*?)\"', res2, re.S).group(1)
        # 获取商品的所有规格id
        color_dict = {}
        for color in etree.HTML(res4).xpath("//div[@id='choose-attr-1']/div[@class='dd']/div"):
            # 颜色名
            key = ''.join(color.xpath("./@data-value"))
            # 颜色对应图片的链接为字典值
            color_dict['%s' % key] = 'https:' + ''.join(color.xpath("./a/img/@src"))
        # pprint.pprint(color_dict)

        sku_list = eval('[' + re.search('colorSize.*?\[(.*?)\]', res4, re.S).group(1) + ']')
        sku_dict = {}
        for sku in sku_list:
            res3 = requests.get(url2, headers=get_headers4(url4), params=get_params3(sku['skuId'], venderId, cat)).text
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
        # pprint.pprint(another_dict)
        product_info['spcification'] = another_dict
        pprint.pprint(product_info)
        product_info_list.append(product_info)
    return product_info_list
