import requests
from lxml import etree
import re
from wszj_spider import get_headers

# url = 'https://www.229289.com/weishang/10/5568.html'
# res = requests.get(url, headers=get_headers(), verify=False)
# res.encoding = "UTF-8"
# html = res.text
#
# wx = re.search('<div.*?list-thumb.*?src=(.*?)alt.*?</a>', html, re.S).group(1).replace('"','')
# print(wx)
# html = etree.HTML(res.text)
# result = ''.join(html.xpath("//div[@class='contact_body']/ul/li[1]/a/text()"))
# # if '女' in result:
# #     print('女')
# # else:
# #     print('男')
# headimg = ''.join(html.xpath("//div[@class='list-thumb']/ul/li[1]/a/img/@src"))
# print(headimg)
# print(result)

uu = 'https://www.229289.com/weishang/10/5532.html'
us = re.search('weishang\/(\d+)\/(\d+)\.html',uu).group(2)
print(us)
# import urllib3
# with open('123' + '.jpg', 'wb') as f:
#     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#     img = requests.get('https://img.229289.com/202005/27/134405871509.jpg.thumb.jpg', verify=False).content
#     f.write(img)
#
# 'https://img.229289.com/202005/27/134405871509.jpg.thumb.jpg  '