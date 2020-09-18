# coding: utf-8

import pprint
# price_dict = {'000000011346312290': '4599.00',
#               '000000011346312294': '4599.00',
#               '000000011346312311': '4599.00',
#               '000000011346312314': '4999.00',
#               '000000011346312321': '4999.00',
#               '000000011346312325': '5799.00',
#               '000000011346312372': '5799.00',
#               '000000011346320878': '4599.00',
#               '000000011346320881': '4599.00',
#               '000000011346320882': '4599.00',
#               '000000011346320883': '4999.00',
#               '000000011346320884': '4999.00',
#               '000000011346320885': '4999.00',
#               '000000011346320886': '4999.00',
#               '000000011346320888': '5799.00',
#               '000000011346320889': '5799.00',
#               '000000011346320890': '5799.00',
#               '000000011346320891': '5799.00'}
#
# color_dict = {'000000011346312290': '黑色',
#               '000000011346312294': '白色',
#               '000000011346312311': '红色',
#               '000000011346320878': '黄色',
#               '000000011346320881': '紫色',
#               '000000011346320882': '绿色'}
#
# img_dict = {
#     '黑色': 'https://imgservice.suning.cn/uimg1/b2c/image/cmZALe6jKdSMNie_2HYUNA.jpg_800w_800h_4e',
#     '白色': 'https://imgservice.suning.cn/uimg1/b2c/image/6N8FHpu4Ftgpj-L_bOLIBA.jpg_800w_800h_4e',
#     '红色': 'https://imgservice.suning.cn/uimg1/b2c/image/PM2SNFFkwtU_Ff_3-4Ykkw.jpg_800w_800h_4e',
#     '黄色': 'https://imgservice.suning.cn/uimg1/b2c/image/yk5cS5DaHJ_5FLonl1oHkg.jpg_800w_800h_4e',
#     '紫色': 'https://imgservice.suning.cn/uimg1/b2c/image/KuxzhclGQHiyIEkV8pAuRA.jpg_800w_800h_4e',
#     '绿色': 'https://imgservice.suning.cn/uimg1/b2c/image/vXjLfFod11vJp7rwgeUrIA.jpg_800w_800h_4e'}
#
# version_dict = {'000000011346312290': '64G',
#                 '000000011346320883': '128G',
#                 '000000011346320890': '256G'}
# merge_dict = {}
# for key1, value1 in version_dict.items():
#     for key2, value2 in img_dict.items():
#         merge_dict["%s" % value1 + '&' + key2] = {'url': '%s' % value2, 'id': '%s' % key1}
# pprint.pprint(merge_dict)

# merge_price = {}
# for key3, value3 in merge_dict.items():
#     if value3['id'] in price_dict:
#         merge_price['%s' % key3] = {'price': '%s' % price_dict['%s' % value3['id']], 'url': '%s' % value3['url']}
# pprint.pprint(merge_price)
# print(min(int(merge_price.values()['price'])))
# price_list = []
# for key4, value4 in merge_price.items():
#     price_list.append(float(value4['price']))
# print(min(price_list))
import requests
import urllib3
from params_list import get_params2
from headers_list import get_headers3

def one_detail(goods_id):
    url2 = "https://m.suning.com/product/0000000000/{}.html".format(goods_id)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res2 = requests.get(url2, params=get_params2(), headers=get_headers3(), verify=False).text
    pprint.pprint(res2)
one_detail('11346312311')


