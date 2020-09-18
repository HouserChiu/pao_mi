# coding: utf-8

import requests
from headers_lists import get_headers2
from params_list import get_params2
import urllib3


def id_page_one(pre_cate, i):
    url = "https://s.taobao.com/search"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=get_headers2(), params=get_params2(pre_cate, i), verify=False).text
    print(res)


if __name__ == '__main__':
    id_page_one('地下城与勇士', 3)


