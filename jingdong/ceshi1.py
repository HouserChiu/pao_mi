# coding: utf-8

import requests
import urllib3
from headers_list import get_headers2
from params_list import get_params1
from lxml import etree
import pprint

url = "https://search.jd.com/s_new.php"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
res = requests.get(url, headers=get_headers2(), params=get_params1()).text
id_list = etree.HTML(res).xpath("//li[@class='gl-item']/@data-sku")
# print(id_list)
pprint.pprint(id_list)



