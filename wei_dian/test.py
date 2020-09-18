import json

import requests
import urllib3
from wd_seller import get_headers
# url = 'https://129010.ixiaochengxu.cc/index.php?s=/addon/DgStore/Api/getStoreList.html&page_index=163&ws_lat=30.651608&ws_lng=104.080275&store_cate=7559&keywords=&utoken=17fd4c76c297a40c9570c8f1302ddbe0&token=gh_f1ed514327ce'
url = 'https://129010.ixiaochengxu.cc/index.php?s=/addon/DgStore/Api/getStoreList.html&page_index=196&ws_lat=30.651608&ws_lng=104.080275&store_cate=7561&keywords=&utoken=17fd4c76c297a40c9570c8f1302ddbe0&token=gh_f1ed514327ce'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
res = json.loads(requests.get(url, headers=get_headers(), verify=False).text)
id_list = []
for temp in res['data']:
    id_list.append(temp['id'])
print(id_list)

