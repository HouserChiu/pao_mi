# # import requests
# import urllib3
# # url = 'https://miyuanserver.top/appc/uploads/headimg/1585678801756.png'
# # with open('123' + '.jpg', 'wb') as f:
# #     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# #
# #     img = requests.get(url,verify=False).content
# #
# #     f.write(img)
#
# # import re
# # uu = 'https://www.229289.com/weishang/10/5532.html'
# # us = re.search('weishang\/(\d+)\/(\d+)\.html',uu).group(2)
# # print(us)
#
# import requests
# from lxml import etree
#
# def get_headers():
#     headers = {
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'zh-CN,zh;q=0.9',
#         'cache-control': 'max-age=0',
#         'cookie': 'cw1_mobile=pc',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'none',
#         'sec-fetch-user': '?1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     }
#     return headers
#
# url = 'https://www.229289.com/weishang/4/'
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# res = requests.get(url, headers=get_headers(), verify=False)
# res.encoding = "UTF-8"
# html = etree.HTML(res.text)
# temp = ''.join(html.xpath("//div[@class='pages']/a[9]/text()")).strip()
# print(temp)


import re
url = 'http://img5.imgtn.bdimg.com/it/u=183326193,1784969774&fm=26&gp=0.jpg'
name = re.search('http.*?\=.*?\.(\d+).*?jpg', url).group(1)
print(name)