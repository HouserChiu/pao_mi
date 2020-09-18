import requests
import urllib3
from lxml import etree
import re

def get_headers():
    headers = {
        'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
        'cookie':'Hm_lvt_a0f9e240fdf94097d93363308f3939ca=1591839700; Hm_lpvt_a0f9e240fdf94097d93363308f3939ca=1591839700; token=ew0KICAidHlwIjogIkpXVCIsDQogICJhbGciOiAiSFMyNTYiDQp9.ew0KICAiVG9rZW5JZCI6ICI4NTQ3Y2Y5MTE1ZjA0YmM0ODVkMTM3NWU2NGEyODY0MyIsDQogICJNZW1iZXJJZCI6IDY3MDUwOTAsDQogICJSYW1JZCI6IDAsDQogICJFeHBpcmVkVGltZSI6ICIyMDIwLTA2LTEyIDA5OjQyOjExIg0KfQ.Ww9PzHiNEqfWIe1C8zCXfD66rmTPOLiuyjuC-LOQ-og; sid=jeekikpgkg53xa4wptumvsvk; SERVERID=9088ee2b3a500e9c1aa86d559c1988a4|1591840045|1591839708',
        'referer':'https://dy.delidou.com/',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'x-requested-with':'XMLHttpRequest',
    }
    return headers

def get_params():
    params_list = []
    for i in range(0, 35):
        params = {
            'cateid': '%s' % i,
            'ajax': '1'
        }
        params_list.append(params)
    return params_list

def one_page():
    params_list = get_params()
    id_lists = []
    for params in params_list:
        url = 'https://dy.delidou.com/rank/user/score'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = requests.get(url, headers=get_headers(), params=params, verify=False).text
        temp = etree.HTML(res)
        id_list = []
        for i in range(0, 10):
            result = ''.join(temp.xpath("//div[@class='id-avatar left']/a/@href")[i])
            eve = re.search('\/.*?(\d+)', result, re.S).group(1)
            id_list.append(eve)
        id_lists.append(id_list)
    print(id_lists)
    # return id_lists
one_page()

# def two_page():
#     idss = one_page()
#     for ids in idss:
#         for id in ids:
#             url = 'https://dy.delidou.com/user/detail/' + str(id)
#             urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#             res = requests.get(url,headers=get_headers(),verify=False).text
#             temp = etree.HTML(res)
#             user_info = {}
#             user_info['platform'] = '7'
#             user_info['avatar'] = res['fdAvatar']
#             user_info['userid'] = id
#             user_info['name'] = res['fdName']
#             user_info['url'] = res['fdLink']
#             user_info['location'] = res['fdArea']
#             user_info['account'] = res['fdCode']
#             if res['fdSex'] == 1:
#                 user_info['sex'] = '1'
#             elif res['fdSex'] == 2:
#                 user_info['sex'] = '2'
#             else:
#                 user_info['sex'] = ''
#             if res['fdConstellation'] == '未知星座':
#                 user_info['stars'] = ''
#             else:
#                 user_info['stars'] = res['fdConstellation']
#             user_info['personal_profile'] = res['fdSignature']
#             user_info['label'] = res['fdLabels']
#
#             if res['fdBirthday'] == 'null' or res['fdBirthday'] == None:
#                 user_info['age'] = ''
#             else:
#                 now_year = datetime.datetime.today().year
#                 birthday = datetime.datetime.strptime(res['fdBirthday'], '%Y-%m-%d %H:%M:%S').year
#                 age = now_year - birthday
#                 user_info['age'] = age
#
#             user_info['mcn'] = res['fdMcnName']
#             user_info['categoryid'] = res['fdLabels']
#             user_info['fans'] = res['fdFansNum']
#             user_info['likes'] = res['fdLikeNum']
#             url1 = 'https://www.luonet.com/api/douyinUserReport/getDataConclude/' + str(id)
#             urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#             res1 = json.loads(requests.get(url1, headers=headers[1], verify=False).text)
#             user_info['production'] = res1['fdPublishTotal']
#             print(user_info)





