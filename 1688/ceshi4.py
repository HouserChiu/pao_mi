import json
import re

import requests

# url = 'https://detail.1688.com/offer/616807053531.html?tracelog=p4p&clickid=5dd78b3d6a78483ca21d36b9c3ae405e&sessionid=d3631d4cae9e76d8185aa48f08f1dd94'
url = 'https://detail.1688.com/offer/533672913646.html?spm=a261y.7663282.trade-type-tab.1.703c2924UUjF8A&sk=consign'

headers = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'cna=l6OSF+T7ey8CAWXPj2rNH0ng; cookie2=1e19fbb8c7b47e704d2ba6dfe61a366b; t=88d50d18c5257c48bde36d3d2b01c5c2; _tb_token_=535ee33a51773; __cn_logon__=false; UM_distinctid=17345bd6a55511-0ad2e6b4175536-4353760-1fa400-17345bd6a569ac; taklid=93aef6e3c22f4a568ff502bae8532e12; _csrf_token=1594602914983; CNZZDATA1253659577=981820121-1594602631-https%253A%252F%252Fp4psearch.1688.com%252F%7C1594625647; alicnweb=touch_tb_at%3D1594625985071; JSESSIONID=C9FB0ADF4929A4C2FC282F2A27CFC132; l=eBMyPz4rOgetekVoBO5anurza77OyIRb8sPzaNbMiInca69fLeJWhNQq9YhBbdtjgt5xMetrb3kJjREBSD4U-PZT-a-XkKXoyB968e1..; isg=BBMTUDBgSDZJDARlAPGXHDw5opc9yKeKNpDodsUw3DJxRDLmTZsl27heerQqZP-C',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}

res = requests.get(url, headers=headers, verify=False).text
# print(res)
try:
    skuProps = '[' + re.search('skuProps.*?\[(.*?)skuMap', res, re.S).group(1).strip().rstrip(',')
    skuMap = '{' + re.search('skuMap.*?\{(.*?)end', res, re.S).group(1).strip().rstrip(',')
    res_eve = json.loads(skuProps)
    res_temp = json.loads(skuMap)
except json.decoder.JSONDecodeError:
    skuProps = '[' + re.search('skuProps.*?\[(.*?)skuMap', res, re.S).group(1).rstrip('"').strip().rstrip(',')
    skuMap = '{' + re.search('skuMap.*?\{(.*?)end', res, re.S).group(1).rstrip('"').strip().rstrip(',').rstrip(
        '}').strip().rstrip(',')
    res_eve = json.loads(skuProps)
    res_temp = json.loads(skuMap)
# print(res_eve)
print(res_temp)

# img_dict = {}
# for value_eve in res_eve:
#     for i in value_eve['value']:
#         # print(i)
#
#         if "imageUrl" in i.keys():
#             img_dict["%s" % i["name"]] = {"price": "", "url": i['imageUrl']}
# print(img_dict)


