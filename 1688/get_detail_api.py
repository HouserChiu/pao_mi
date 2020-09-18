# coding: utf-8

import os
import time
from lxml import etree
import requests
import urllib3
import re
import json
from headers_lists import get_headers3, get_headers4, get_headers5, get_headers7, get_headers8, get_headers9, \
    get_headers2, get_headers10
from params_lists import get_params2, get_params3, get_params4
from info_mongoimport import mongo_info_alibaba
from handle_template import format_html


def get_detail(goods_id):
    url = 'https://detail.1688.com/offer/{}.html?sk=consign'.format(goods_id)
# def get_detail():
#     url = 'https://detail.1688.com/offer/613654393509.html?spm=a261y.7663282.trade-type-tab.1.5da4782dOfHcXf&sk=consign'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=get_headers10(), verify=False, timeout=None, allow_redirects=False).text
    product_info = {}
    product_info['title'] = ''.join(etree.HTML(res).xpath("//html[@lang='zh-CN']/head/title/text()"))
    product_info['shop_name'] = re.search('<meta.*?og:product:nick.*?name=(.*?);.*?>', res, re.S).group(1)
    product_info['goods_id'] = re.search('<meta.*?b2c_auction.*?content=\"(\d+)\".*?>', res, re.S).group(1)
    product_info['source'] = url
    # 商品图，创建product_img文件夹并下载图片
    product_info['imgsSrc'] = re.findall('<li.*?tab-trigger.*?original\"\:\"(.*?)\"', res, re.S)
    # os.chdir('C:/Users/admin/Desktop/1688')
    # if os.path.exists('./6/' + '%s' % product_info['goods_id']) == False:
    #     os.makedirs('./6/' + '%s' % product_info['goods_id'] + '/product_img')
    #     os.chdir('C:/Users/admin/Desktop/1688/6/' + '%s' % product_info['goods_id'] + '/product_img')
    #     i = 1
    #     for temp_img in product_info['imgsSrc']:
    #         with open('%s' % i + '.jpg', 'wb') as f:
    #             urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #             eve_image = requests.get(temp_img, verify=False).content
    #             f.write(eve_image)
    #             i += 1

        # 视频页面,创建product_video文件夹并下载视频
    memberId = re.search('member_id.*?\"(.*?)\"', res, re.S).group(1)
    videoId = re.search('videoId.*?\"(\d+)\"', res, re.S).group(1)
    if videoId != '0':
        res2 = requests.get('https://apps.1688.com/event/app/videoInfo/getVideoById.htm',
                            params=get_params3(videoId, memberId), headers=get_headers4(), verify=False).text
        product_info['videoUrl'] = re.search('address\"\:\"(.*?)\"', res2, re.S).group(1)

        # os.chdir('C:/Users/admin/Desktop/1688/6/' + '%s' % product_info['goods_id'])
        # os.mkdir('./product_video')
        # os.chdir('C:/Users/admin/Desktop/1688/6/' + '%s' % product_info['goods_id'] + '/product_video')
        # with open('%s' % product_info['goods_id'] + '.mp4', 'wb') as f:
        #     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        #     video = requests.get(product_info['videoUrl'], verify=False).content
        #     f.write(video)
    try:
        # 分销、代发页面
        # url3 = 'https://detail.1688.com/offer/{}.html?sk=consign'.format(product_info['goods_id'])
        # res3 = requests.get(url3, headers=get_headers7(product_info['goods_id']), verify=False,
        #                     allow_redirects=False, timeout=None).text
        # 是否有分销界面解析规则不一样
        try:
            skuProps = '[' + re.search('skuProps.*?\[(.*?)skuMap', res, re.S).group(1).rstrip('"').strip().rstrip(
                ',')
            skuMap = '{' + re.search('skuMap.*?\{(.*?)end', res, re.S).group(1).rstrip('"').strip().rstrip(
                ',').rstrip(
                '}').strip().rstrip(',')
            Specifications1 = json.loads(skuProps)
            Specifications2 = json.loads(skuMap)

        except json.decoder.JSONDecodeError:
            skuProps = '[' + re.search('skuProps.*?\[(.*?)skuMap', res, re.S).group(1).rstrip('"').strip().rstrip(
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
            fee = res_eve['data']['data']['offerdetail_ditto_postage']['freightCost'][0]['costItems'][0]['value']
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
        # 创建规格文件夹颜色
        # os.chdir('C:/Users/admin/Desktop/1688/6/' + '%s' % product_info['goods_id'])
        # os.makedirs('./product_specifications/color')
        # os.chdir(
        #     'C:/Users/admin/Desktop/1688/6/' + '%s' % product_info['goods_id'] + '/product_specifications/color')
        # with open('%s' % product_info['goods_id'] + '.json', 'w') as fp:
        #     fp.write(json.dumps(price_dict, indent=4, ensure_ascii=False))
        # for key3, value3 in price_dict.items():
        #     with open('%s' % key3 + '.jpg', 'wb') as f:
        #         urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        #         if "https" in value3['url']:
        #             specification_img = requests.get(value3['url'], verify=False).content
        #             f.write(specification_img)
        # 尺寸
        # if len(Specifications1) >= 2:
        #     os.chdir('C:/Users/admin/Desktop/1688/6/' + '%s' % product_info['goods_id'])
        #     os.makedirs('./product_specifications/size')
        #     os.chdir(
        #         'C:/Users/admin/Desktop/1688/6/' + '%s' % product_info['goods_id'] + '/product_specifications/size')
        #     for key4 in Specifications1:
        #         for kk_eve in key4['value']:
        #             with open('%s' % kk_eve['name'].replace("/", "").replace("*", "") + '.txt', 'w') as f:
        #                 f.write('1')
    except AttributeError:
        pass

    # 富文本图链接
    # html_url = re.search('data-tfs-url=\"(.*?)\"', res, re.S).group(1)
    # params = {'t': '%s' % int(round(time.time() * 1000))}
    # res1 = requests.get(html_url, headers=get_headers5(), params=params, verify=False).text.replace('\\', '')

    # 匹配图片用于富文本构造
    # result = re.findall('alt.*?src=\"(.*?)\"', res1, re.S)
    # file = 'C:/Users/admin/Desktop/1688/html_template.html'
    # saveHtmlFilePath = 'C:/Users/admin/Desktop/1688/6/' + '%s' % product_info['goods_id'] + '/' + '%s' % \
    #                    product_info[
    #                        'goods_id'] + '.html'
    # 参数依次为富文本模板，保存路径，图片列表
    # format_html(file, saveHtmlFilePath, result)
    # print(product_info)
    return product_info
# get_detail()
