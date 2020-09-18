import json
import time

import requests
from spider import get_headers
url = 'https://openapi.qian-gua.com/v1/Blogger/GetDetail?bloggerId=1240536&dateCode=20200611&_={}'.format(int(round(time.time() * 1000)))
res = json.loads(requests.get(url,headers=get_headers()).text)
for province_info in res['Data']['BloggerFansInfo']['ProvinceList']:
    province_infos = {}
    province_infos['province'] = province_info['Name']
    province_infos['percentage'] = province_info['Percent']
    print(province_infos)