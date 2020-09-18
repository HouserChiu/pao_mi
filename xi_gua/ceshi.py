import requests
import json
import time
from web_spider import get_headers
from lxml import etree


# def get_params():
#     bizid_list = []
#     key_list = []
#     url = 'http://data.xiguaji.com/rank/IndustryNew/'
#     params = {
#         'tid':'17',
#         'pageIndex':'1',
#         'isPart':'true',
#         'period':'1',
#         'statDateCode':'20200614',
#         'menuClick':'true',
#     }
#     res = requests.get(url,params=params,headers=get_headers()).text
#     trs = etree.HTML(res)
#     for tr in trs:
#         bizid = ''.join(tr.xpath(".//span[@class='js-rank-detail-btn']/@data-bizid"))
#         key = ''.join(tr.xpath(".//span[@class='js-rank-detail-btn']/@data-key"))
#         bizid_list.append(bizid)
#         key_list.append(key)
#     print(bizid_list)
#     print(key_list)
#     return bizid_list, key_list
#
# get_params()
def get_two():
    url = 'http://data.xiguaji.com/Search/Detail?bizId=758&key=61539e'
    res = requests.get(url, headers=get_headers()).text
    user_info = {}
    user_info['avatar'] = ''.join(etree.HTML(res).xpath("//div[@class='number-logo']/img/@src"))
    user_info['name'] = ''.join(etree.HTML(res).xpath("//div[@class='number-details']/h3/text()"))
    user_info['account'] = ''.join(etree.HTML(res).xpath("//div[@class='btns-group']/a[2]/@data-wid"))
    user_info['categoryid'] = ''.join(etree.HTML(res).xpath("//div[@class='function-decribe']/p[1]/text()")).strip()
    if ''.join(etree.HTML(res).xpath("//div[@class='function-decribe']/p[2]/text()")).strip() == '--':
        user_info['location'] = ''
    else:
        user_info['location'] = ''.join(etree.HTML(res).xpath("//div[@class='function-decribe']/p[2]/text()")).strip()
    if ''.join(etree.HTML(res).xpath("//div[@class='similar-publicnum']/p/text()")).strip() == "个人":
        user_info['mcn'] = ''
    else:
        user_info['mcn'] = ''.join(etree.HTML(res).xpath("//div[@class='similar-publicnum']/p/text()")).strip()

    fans = ''.join(etree.HTML(res).xpath("//ul[@class='recent-statistics-chart clearfix']/li[1]/text()")).strip()
    if '万' in fans:
        user_info['fans'] = int(float(fans.split('万')[0]) * 10000)
    else:
        user_info['fans'] = ''.join(etree.HTML(res).xpath("//ul[@class='recent-statistics-chart clearfix']/li[1]/text()")).strip()
    user_info['production'] = ''.join(etree.HTML(res).xpath("//ul[@class='recent-statistics-chart clearfix']/li[2]/text()")).strip()
    user_info['signature'] = ''.join(etree.HTML(res).xpath("//p[@class='p-biz-desc']/text()")).strip()
    user_info['signature'] = ''.join(etree.HTML(res).xpath("//p[@class='p-biz-desc']/text()")).strip()
    print(user_info)
get_two()