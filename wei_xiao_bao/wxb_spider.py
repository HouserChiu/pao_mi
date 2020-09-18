'''
带货达人榜
需要更新cookie
'''
import requests
import json
import datetime
import urllib3
import urllib.parse
from mongo_info import mongo_info_wxb
import time

def get_headers():
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'RMU=4823202; RMT=a1aa675f7a96eb7f835773550a4c3d47; PHPSESSID=5d761098641bd45d0d9dc76aed2063b9; Hm_lvt_5859c7e2fd49a1739a0b0f5a28532d91=1590634867,1590980591,1590994850,1591067616; Qs_lvt_288791=1590994850%2C1591067615%2C1591067621; Qs_pv_288791=2062370387508984300%2C879614537376331400%2C3657084777334233600%2C4577741676427161600; aliyungf_tc=AQAAAH7ZgSRnzg0Aa1LR3nVUn6vaXIkG; Hm_lpvt_5859c7e2fd49a1739a0b0f5a28532d91=' + str(int(time.time())),
        'Host': 'data.wxb.com',
        'Referer': 'https://data.wxb.com/rank',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    return headers


def get_cate():
    url = 'https://data.wxb.com/rank/articleCatalog'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = json.loads(requests.get(url, headers=get_headers(), verify=False).text)
    cate_list = []
    for cate in res['data']:
        cate_list.append(cate)
    return cate_list



def get_params():
    params_list = []
    for i in range(1, 7):
        params_list.append({'sort': '', 'page': '%s' % i, 'page_size': '50', 'is_new': '1', })
    return params_list


def one_page():
    cates = get_cate()
    paramss = get_params()
    wx_id_lists = []
    for cate in cates:
        url = "https://data.wxb.com/rank/day/" + str(((datetime.datetime.now() + datetime.timedelta(days=-2)).strftime(
            '%Y-%m-%d'))) + "/" + "%s" % urllib.parse.quote(cate)
        for params in paramss:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res_temp = requests.get(url, params=params, headers=get_headers(), verify=False, timeout=None).text
            print(cate)
            print(params)
            print(res_temp)
            try:
                res = json.loads(res_temp)
                wx_id_list = []
                for wxid in res['data']:
                    wx_id_list.append(wxid['wx_origin_id'])
                wx_id_lists.append(wx_id_list)
            except json.decoder.JSONDecodeError:
                pass
            # res = json.loads(res_temp)
            # wx_id_list = []
            # for wxid in res['data']:
            #     wx_id_list.append(wxid['wx_origin_id'])
            # wx_id_lists.append(wx_id_list)
            # wx_id_list = []
            # for wxid in res['ids']:
            #     wx_id_list.append(wxid)
            # wx_id_lists.append(wx_id_list)
    # print(wx_id_lists)
    return wx_id_lists


def two_page():
    wxidss = one_page()
    for wxids in wxidss:
        for wxid in wxids:
            url = 'https://data.wxb.com/account/index/{}?is_new=1'.format(wxid)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            try:
                res = json.loads(requests.get(url, headers=get_headers(), verify=False, timeout=None).text)
                user_info = {}
                user_info['platform'] = '3'
                user_info['name'] = res['data']['name']
                user_info['avatar'] = res['data']['avatar']
                user_info['sex'] = ''
                user_info['stars'] = ''
                user_info['age'] = ''
                user_info['location'] = ''
                # 功能介绍
                user_info['personal_profile'] = res['data']['desc']
                # 微信公众号id
                user_info['account'] = res['data']['wx_alias']
                # 第三方id
                user_info['userid'] = wxid
                # 所属分类
                user_info['categoryid'] = res['data']['current_cat']
                # 小宝指数
                # user_info['index_scores'] = res['data']['index_scores']
                # 预估粉丝数
                user_info['fans'] = res['data']['fans_num_estimate']
                user_info['likes'] = res['data']['fans_num_estimate']
                user_info['url'] = res['data']['fans_num_estimate']
                user_info['production'] = res['data']['fans_num_estimate']
                # 账号主体
                user_info['mcn'] = res['data']['company']
                user_info['label'] = res['data']['category_name']
                # 公众号二维码
                # user_info['qrcode'] = res['data']['qrcode']
                # 数据更新时间
                # user_info['stat_time'] = res['data']['stat_time']
                # user_info['customer_type'] = res['data']['customer_type']
                # user_info['label'] = res['data']['tags']
                # 公众号二维码
                # user_info['qrcode'] = res['data']['qrcode']
                # user_info['is_weixin_verify'] = res['data']['is_weixin_verify']
                # user_info['is_original'] = res['data']['is_original']
                # user_info['uin'] = res['data']['uin']

                # url2 = 'https://data.wxb.com/account/stat/{}'.format(wxid)
                # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                # res2 = json.loads(requests.get(url2, headers=get_headers(), verify=False).text)
                # user_info['avg_watching'] = res2['data']['avg_like_num_idx1']
                # user_info['max_watching'] = res2['data']['max_like_latest_30']
                # 头条平均阅读数
                # user_info['avg_read_num_idx1'] = res2['data']['avg_read_num_idx1']
                # 非头条平均阅读数
                # user_info['avg_read_num_non_top'] = res2['data']['avg_read_num_non_top']
                # 最高阅读数
                # user_info['max_read_latest_30'] = res2['data']['max_read_latest_30']
                # 阅读时间段
                # user_info['push_time_solt'] = res2['data']['push_time_solt']
                print(user_info)
                mongo_info_wxb.insert_item(user_info)
            except json.decoder.JSONDecodeError:
                pass
            # res = json.loads(requests.get(url, headers=get_headers(), verify=False, timeout=None).text)
            # user_info = {}
            # user_info['name'] = res['data']['name']
            # user_info['avatar'] = res['data']['avatar']
            # # 功能介绍
            # user_info['desc'] = res['data']['desc']
            # # 微信公众号id
            # user_info['wx_alias'] = res['data']['wx_alias']
            # # 第三方id
            # user_info['wx_origin_id'] = res['data']['wx_origin_id']
            # # 所属分类
            # user_info['current_cat'] = res['data']['current_cat']
            # # 小宝指数
            # user_info['index_scores'] = res['data']['index_scores']
            # # 预估粉丝数
            # user_info['fans'] = res['data']['fans_num_estimate']
            # # 账号主体
            # user_info['company'] = res['data']['company']
            # user_info['category_name'] = res['data']['category_name']
            # # 公众号二维码
            # user_info['qrcode'] = res['data']['qrcode']
            # # 数据更新时间
            # user_info['stat_time'] = res['data']['stat_time']
            # user_info['customer_type'] = res['data']['customer_type']
            # user_info['tags'] = res['data']['tags']
            # user_info['qrcode'] = res['data']['qrcode']
            # user_info['is_weixin_verify'] = res['data']['is_weixin_verify']
            # user_info['is_original'] = res['data']['is_original']
            # user_info['uin'] = res['data']['uin']
            #
            # url2 = 'https://data.wxb.com/account/stat/{}'.format(wxid)
            # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            # res2 = json.loads(requests.get(url2, headers=get_headers(), verify=False).text)
            # user_info['avg_watching'] = res2['data']['avg_like_num_idx1']
            # user_info['max_watching'] = res2['data']['max_like_latest_30']
            # # 头条平均阅读数
            # user_info['avg_read_num_idx1'] = res2['data']['avg_read_num_idx1']
            # # 非头条平均阅读数
            # user_info['avg_read_num_non_top'] = res2['data']['avg_read_num_non_top']
            # # 最高阅读数
            # user_info['max_read_latest_30'] = res2['data']['max_read_latest_30']
            # # 阅读时间段
            # user_info['push_time_solt'] = res2['data']['push_time_solt']
            # print(user_info)
            # mongo_info_wxb.insert_item(user_info)


two_page()
