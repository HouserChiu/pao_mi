'''
千瓜行业榜
'''
import requests
import json
import time
from mongo_info import mongo_info_xhs


def get_params():
    tagIds = [0, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 100,
              102]
    params_list = []
    for tagId in tagIds:
        params = {
            'pageSize': '50',
            'pageIndex': '1',
            'search': '',
            'dateCode': '20200514',
            'period': '1',
            'rankType': '12',#品牌豪排行榜改为13,mcn榜为45，没有tagId
            'tagId': '%d' % tagId,
            '_': '%s' % int(round(time.time() * 1000)),
        }
        params_list.append(params)
    return params_list



def get_headers():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'User=UserId=c5ad0398af02d74f&Password=bc15b86050ac8c5c2378ccaa38259425&ChildId=0; _data_chl=key=BaiduOrginal; Hm_lvt_c6d9cdbaf0b464645ff2ee32a71ea1ae=1589339141,1589420317,1589506495; ASP.NET_SessionId=mymzolhhprtwwcqtna3dsq55; Hm_lpvt_c6d9cdbaf0b464645ff2ee32a71ea1ae=1589512999',
        'Host': 'api.qian-gua.com',
        'Origin': 'http://app.qian-gua.com',
        'Referer': 'http://app.qian-gua.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    return headers


def two_stage_params():
    params_list = get_params()
    BloggerId_lists = []
    BloggerIdKey_lists = []
    for params in params_list:
        url = 'http://api.qian-gua.com/Rank/GetBloggerRank'
        # mcn榜的url
        # url = 'http://api.qian-gua.com/Rank/GetMcnRankData'
        res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
        ItemList = res['Data']['ItemList']
        BloggerId_list = []
        BloggerIdKey_list = []
        for itemlist in ItemList:
            BloggerId_list.append(itemlist['BloggerId'])
            BloggerIdKey_list.append(itemlist['BloggerIdKey'])
        BloggerId_lists.append(BloggerId_list)
        BloggerIdKey_lists.append(BloggerIdKey_list)
    return BloggerId_lists, BloggerIdKey_lists


def get_detail():
    BloggerIdss = two_stage_params()[0]
    BloggerIdKeyss = two_stage_params()[1]

    for BloggerIds, BloggerIdKeys in zip(BloggerIdss, BloggerIdKeyss):
        for BloggerId, BloggerIdKey in zip(BloggerIds, BloggerIdKeys):
            params = {
                'bloggerId': '%s' % BloggerId,
                'sign': '%s' % BloggerIdKey,
                '_': '%s' % int(round(time.time() * 1000)),
            }
            url = 'http://api.qian-gua.com/blogger/GetDetail'
            user_infos = json.loads(requests.get(url, headers=get_headers(), params=params).text)
            user_info = {}
            # 小红书平台为3
            user_info['platform'] = '3'
            # 头像
            user_info['BigAvatar'] = user_infos['Data']['BigAvatar']
            # 地区
            user_info['Location'] = user_infos['Data']['Location']
            # 等级
            user_info['LevelName'] = user_infos['Data']['LevelName']
            # 所属机构
            user_info['McnName'] = user_infos['Data']['McnName']
            # 属性
            user_info['BloggerProp'] = user_infos['Data']['BloggerProp']
            # 粉丝数
            user_info['Fans'] = user_infos['Data']['Fans']
            # 点赞数
            user_info['Liked'] = user_infos['Data']['Liked']
            # 收藏数
            user_info['Collected'] = user_infos['Data']['Collected']
            user_info['CommentNum'] = user_infos['Data']['CommentNum']
            # 千瓜指数
            user_info['BloggerIndex'] = user_infos['Data']['BloggerIndex']
            # 图文笔记
            user_info['NoteNormalCount'] = user_infos['Data']['NoteNormalCount']
            # 视频笔记
            user_info['NoteVideoCount'] = user_infos['Data']['NoteVideoCount']
            # 标签
            TagLists = user_infos['Data']['TagList']
            for TagList in TagLists:
                user_info['TagName'] = TagList['TagName']
            # 性别
            if user_infos['Data']['Gender'] == 1:
                user_info['Gender'] = '女'
            else:
                user_info['Gender'] = '男'
            # 是否品牌合作人
            if user_infos['Data']['IsBrandPartner'] == 'true':
                user_info['IsBrandPartner'] = '是'
            else:
                user_info['IsBrandPartner'] = '否'
            # Id
            user_info['RedId'] = user_infos['Data']['RedId']
            print(user_info)
            mongo_info_xhs.insert_item(user_info)


get_detail()
