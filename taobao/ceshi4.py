# coding: utf-8
import json
import re

import requests
import time
import urllib.parse

url = "https://mdskip.taobao.com/core/initItemDetail.htm"
headers = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cookie': 'cookie2=15faf29f2f38e3f2581b9605f0e05d72; t=5732c367f5712218ae648ea918524789; _tb_token_=ee54b505e697d; _samesite_flag_=true; v=0; cna=8FmVF+VBJxgCAd7RUm5VHyu7; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; sgcookie=EVwWMJ0cBzsKngrzD6ay%2B; unb=1046815482; uc3=nk2=F5RHpr11toKZszuTPfk%3D&vt3=F8dBxGPiAl7wpruyZBE%3D&id2=UoH7LXuyKB0VPQ%3D%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; csg=b0284fd0; lgc=tb2718229_2012; cookie17=UoH7LXuyKB0VPQ%3D%3D; dnk=tb2718229_2012; skt=0e503ab5c294a608; existShop=MTU5NTM4NDExNQ%3D%3D; uc4=id4=0%40UOnkSQ%2Fs2F54PslpQqrfotjQS2mr&nk4=0%40FY4MtLzu6TOXXT69SO8b0hhFA49cfDqHdg%3D%3D; tracknick=tb2718229_2012; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=227; _nk_=tb2718229_2012; cookie1=ACqzrkP8OHp7Gasg2fIdhVDOYZZmwSVn4Zy6%2FaMpVcU%3D; enc=z5Nw70IMyGUxAg8deEXSSe3%2FIMOgZDvIw2K3hppE7k2jepiLe9AdFQnbTKnhui7wpqmRV6xPl9BPdM7%2FMaKi0Q%3D%3D; mt=ci=0_1; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie14=UoTV6e6LO5E1nw%3D%3D&pas=0&existShop=false&cookie15=VT5L2FSpMGV7TQ%3D%3D&cookie21=VT5L2FSpccLuJBreK%2BBd; ucn=center; tfstk=c4mdBAfV2CAnlr2t32LgN8iaWlRcawR819Nl2L2KHo1waZsc0sxZmm3boew58XvO.; isg=BGxsu4mvHyhjhwsNoh185P87PUqeJRDPQtNkLcatepe60Qzb7jR_X2Tg8Znp2Ugn; l=eBTnmTKrOLp9Xx8TBOfZnurza779IIRAguPzaNbMiOCPOaCB5VGRWZklzZY6CnGVh6kDR3oIr-vXBeYBquE-nxvOvhLyCdDmn',
'referer': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.27.5a9e2b71hb2OPd&id=621848137263&ns=1&abbucket=3&sku_properties=10004:709990523;5919063:6536025;12304035:3222911',
'sec-fetch-dest': 'script',
'sec-fetch-mode': 'no-cors',
'sec-fetch-site': 'cross-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
}
params = {
'isUseInventoryCenter': 'false',
'cartEnable': 'true',
'service3C': 'true',
'isApparel': 'false',
'isSecKill': 'false',
'tmallBuySupport': 'true',
'isAreaSell': 'false',
'tryBeforeBuy': 'false',
'offlineShop': 'false',
'itemId': '620611076986',
'showShopProm': 'false',
'isPurchaseMallPage': 'false',
'itemGmtModified': '1595365357000',
'isRegionLevel': 'false',
'household': 'false',
'sellerPreview': 'false',
'queryMemberRight': 'true',
'addressLevel': '4',
'isForbidBuyItem': 'false',
'callback': 'setMdskip',
'timestamp': '%s' % int(round(time.time() * 1000)),
'isg': 'eBgEr4XeONpsdemdBO5aourza7796IRb8sPzaNbMiInca1kf9eOFFNQqEa-eWdtjgt5xmetrA42DhRneSz438PkDBeYCKXIpBjv68e1..',
'isg2': 'BKioBitmY1w_Rk_ZyVK73OV0eZa60Qzbvi-g4WLZBCMQvUknCuKNai88sVVNjcSz',
'ref': 'https://s.taobao.com/search?spm=a21bo.2017.201867-links-3.53.14a711d9DzC989&q=%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200420&ie=utf8',
}

res = requests.get(url, headers=headers, params=params).text
print(res)
res_temp = '{' + re.search('defaultModel.*?\{(.*?)isSuccess', res, re.S).group(1).rstrip('"').strip().rstrip(',')
res_eve = json.loads(res_temp)
if res_eve['deliveryDO']['deliverySkuMap']['default'][0]['postageFree'] == False:
    postage = float(res_eve['deliveryDO']['deliverySkuMap']['default'][0]['postage'].split(':')[1])
else:
    postage = float(res_eve['deliveryDO']['deliverySkuMap']['default'][0]['money'])