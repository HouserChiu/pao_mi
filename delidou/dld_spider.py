import re
import requests
import json
import urllib3
from lxml import etree

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
# url = 'https://dy.delidou.com/user/detail/persona/104255897823'
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# res = requests.get(url,headers=headers,verify=False).text
# result = '[' + re.search('JSON\.parse.*?\[(.*?)\].*?\,', res, re.S).group(1) + ']'
# rate = '[' + re.search('genderRangeData.*?y1.*?\[(.*?)\].*?\,', res, re.S).group(1) + ']'
# eve1 = eval(result)
# eve2 = eval(rate)
# for age, age_rate in zip(eve1, eve2):
#     age_infos = {}
#     age_infos['age'] = age
#     age_infos['percentage'] = age_rate
#     print(age_infos)
#     print(type(age_rate))

url = 'https://dy.delidou.com/user/detail/66598046050'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
res = requests.get(url,headers=headers,verify=False).text
# print(res)
# 昵称
print(''.join(etree.HTML(res).xpath("//dt/text()")).strip())
# account
print(''.join(etree.HTML(res).xpath("//dd[1]/text()")).split('：')[1])
# 性别
print(''.join(etree.HTML(res).xpath("//dd[2]/text()")).split('：')[1])
# 地区
try:
    print(''.join(etree.HTML(res).xpath("//dd[3]/span/text()")).split('：')[1])
except IndexError:
    pass
# 分类
print(''.join(etree.HTML(res).xpath("//dd[4]/span/text()")))
# 简介
user_info = {}
sig = (''.join(etree.HTML(res).xpath("//div[@class='id-introductio']/text()")).split('：')[1])
user_info['sig'] = sig
print(user_info)
# 头像
print(''.join(etree.HTML(res).xpath("//div[@class='id-pic left']/img/@src")))
# 标签
print(''.join(etree.HTML(res).xpath("//div[@class='tag-box']/span/text()")))
# 粉丝总数
print(''.join(etree.HTML(res).xpath("//p[@class='data-value']/text()")[0]))
# 作品总数
print(''.join(etree.HTML(res).xpath("//p[@class='data-value']/text()")[1]))
# 点赞总数
print(''.join(etree.HTML(res).xpath("//p[@class='data-value']/text()")[2]))

