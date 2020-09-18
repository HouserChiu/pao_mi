# coding: utf-8

import requests
import urllib3
import re
import json
from headers_lists import get_headers1

def cate_one_plus():
    url = "https://tce.alicdn.com/api/data.htm?ids=222887%2C222890%2C222889%2C222886%2C222906%2C222898%2C222907%2C222885%2C222895%2C222878%2C222908%2C222879%2C222893%2C222896%2C222918%2C222917%2C222888%2C222902%2C222880%2C222913%2C222910%2C222882%2C222883%2C222921%2C222899%2C222905%2C222881%2C222911%2C222894%2C222920%2C222914%2C222877%2C222919%2C222915%2C222922%2C222884%2C222912%2C222892%2C222900%2C222923%2C222909%2C222897%2C222891%2C222903%2C222901%2C222904%2C222916%2C222924&callback=tbh_service_cat"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=get_headers1(), verify=False).text
    result_eve = re.findall('name\"\:\"(.*?)\"', res, re.S)
    # print(result_eve)
    return result_eve
# cate_one()





