# coding: utf-8

import requests

url = "https://s.taobao.com/list?q=%E6%B1%89%E6%9C%8D&cat=16&style=grid&seller_type=taobao&spm=a219r.lm874.1000187.1"

headers = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'thw=cn; cookie2=11baad53f0e72b068205987923f6a275; t=2860081a67b697359e9c35a3d908fa6f; _tb_token_=ee8d7fe63eee3; cna=8FmVF+VBJxgCAd7RUm5VHyu7; _samesite_flag_=true; v=0; _m_h5_tk=623cd64fcb41d527e761debdebd1f323_1594991869788; _m_h5_tk_enc=d4bf75f5056f796ec943a3d4622f0901; sgcookie=EAmJODYSalo2D38S44REt; unb=1046815482; uc3=vt3=F8dBxGPjYkLSvJHtcQg%3D&id2=UoH7LXuyKB0VPQ%3D%3D&lg2=UtASsssmOIJ0bQ%3D%3D&nk2=F5RHpr11toKZszuTPfk%3D; csg=131989df; lgc=tb2718229_2012; cookie17=UoH7LXuyKB0VPQ%3D%3D; dnk=tb2718229_2012; skt=6dabb9036b7d770a; existShop=MTU5NTIwOTA4MA%3D%3D; uc4=id4=0%40UOnkSQ%2Fs2F54PslpQqrfo59Z8n0v&nk4=0%40FY4MtLzu6TOXXT69SO8b0hhFA47t79rzoQ%3D%3D; tracknick=tb2718229_2012; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=227; _nk_=tb2718229_2012; cookie1=ACqzrkP8OHp7Gasg2fIdhVDOYZZmwSVn4Zy6%2FaMpVcU%3D; enc=CYSg0CkEut0iBtryO6OkfuTPQqsgw6kBg6bqNR%2Fe7hoBnAPKw0OnvQdfRmDG0XC2ZeBjbya34%2By%2F%2FtaJ0vR%2BgA%3D%3D; JSESSIONID=D1CD27A4421DFC3CA65D176DADC3C2A8; birthday_displayed=1; tfstk=cR3CBpYcF9XBb8tP8XOaLDR4r4UPaMCbNHwnOcJIGNhFKhh7Bsbfu-NNt0XR_bV1.; l=eBTnmTKrOLp9XjLLXOfanurza77OSIRYYuPzaNbMiOCP9a5B5kFAWZkJcUL6C3GVh6JWR3oIr-vXBeYBq7VonxvO8asD9BHmn; isg=BD09yn3aPkgex5o-u7K9p6YcTJk32nEsKxSVvv-CehTDNl1oxylq_bJk5Gpwtonk; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=0_1; uc1=existShop=false&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie14=UoTV6e9rTyGs4A%3D%3D&pas=0&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D',
'referer': 'https://s.taobao.com/list?q=%E6%B1%89%E6%9C%8D&cat=16&style=grid&seller_type=taobao&spm=a219r.lm874.1000187.1',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
}

res = requests.get(url, headers=headers, verify=False).text
print(res)