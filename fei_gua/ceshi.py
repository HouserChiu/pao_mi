import json
from android_spider import get_headers
import requests
import urllib3
url = 'https://miniapi.feigua.cn/api/v1/blogger/detail?sessionId=42687328977748de9f01d3ff0530271c&id=6585550&sign=172e'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
res = json.loads(requests.get(url, headers=get_headers(), verify=False).text)
user_info = {}
user_info['platform'] = '10'
user_info['avatar'] = res['Data']['BloggerInfo']['Avatar']
user_info['userid'] = id
user_info['name'] = res['Data']['BloggerInfo']['NickName']
user_info['url'] = ''

if res['Data']['BloggerInfo']['Location'] == '未知':
    user_info['location'] = ''
else:
    user_info['location'] = res['Data']['BloggerInfo']['Location']

user_info['account'] = res['Data']['BloggerInfo']['UniqueId']
if res['Data']['BloggerInfo']['Gender'] == '男':
    user_info['sex'] = '1'
elif res['Data']['BloggerInfo']['Gender'] == '女':
    user_info['sex'] = '2'
else:
    user_info['sex'] = ''
if res['Data']['BloggerInfo']['Constellation'] == '未知':
    user_info['stars'] = ''
else:
    user_info['stars'] = res['Data']['BloggerInfo']['Constellation']
user_info['personal_profile'] = res['Data']['BloggerInfo']['Signature']
user_info['label'] = res['Data']['BloggerInfo']['Tags']

if res['Data']['BloggerInfo']['Age'] == '未知':
    user_info['age'] = ''
else:
    user_info['age'] = res['Data']['BloggerInfo']['Age']

user_info['mcn'] = ''
user_info['categoryid'] = user_info['label']
fans = float(res['Data']['BloggerInfo']['MPlatform_Fans'].split('w')[0])
user_info['fans'] = int(fans * 10000)
if 'w' in res['Data']['BloggerInfo']['LikeCount']:
    likes = res['Data']['BloggerInfo']['LikeCount'].split('w')[0]
    user_info['likes'] = int(float(likes) * 10000)
else:
    likes1 = res['Data']['BloggerInfo']['LikeCount'].split('亿')[0]
    user_info['likes'] = int(float(likes1) * 100000000)
user_info['production'] = res['Data']['BloggerInfo']['Awemes']
print(user_info)

# 获得省份信息
if res['Data']['Persona'] != None and res['Data']['Persona']['City'] != []:
    for province_info in res['Data']['Persona']['Province']:
        province_infos = {}
        province_infos['userid'] = id
        province_infos['province'] = province_info['Name']
        province_infos['percentage'] = float(str(province_info['Ratio']).split('%')[0])
        print(province_infos)


# 获取城市信息
if res['Data']['Persona'] != None and res['Data']['Persona']['City'] != []:
    for city_info in res['Data']['Persona']['City']:
        city_infos = {}
        city_infos['userid'] = id
        city_infos['city'] = city_info['Name']
        city_infos['percentage'] = float(str(city_info['Ratio']).split('%')[0])
        print(city_infos)


# 获取年龄信息
if res['Data']['Persona'] != None and res['Data']['Persona']['City'] != []:
    fans_list = []
    for temp in res['Data']['Persona']['Age']:
        fans_list.append(temp['value'])
    eve = sum(fans_list)

    for age_info in res['Data']['Persona']['Age']:
        age_infos = {}
        age_infos['userid'] = id
        age_infos['age'] = age_info['name']
        age_infos['percentage'] = round(age_info['value'] / eve * 100, 2)
        print(age_infos)


# 获取星座信息
if res['Data']['Persona'] != None and res['Data']['Persona']['City'] != []:
    for stars_info in res['Data']['Persona']['Constellation']:
        stars_infos = {}
        stars_infos['userid'] = id
        stars_infos['stars_name'] = stars_info['Name']
        stars_infos['percentage'] = float(str(stars_info['Ratio']).split('%')[0])
        print(stars_infos)

# 获得性别信息
if res['Data']['Persona'] != None and res['Data']['Persona']['City'] != []:
    sex_infos = {}
    sex_infos['userid'] = id
    sex_infos['female_rate'] = float(str(res['Data']['Persona']['Gender'][1]).split('%')[0])
    sex_infos['male_rate'] = float(str(res['Data']['Persona']['Gender'][0]).split('%')[0])
    print(sex_infos)
