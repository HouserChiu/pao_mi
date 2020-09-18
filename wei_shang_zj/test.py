import requests
import urllib3
from lxml import etree


def get_headers():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'cw1_mobile=pc',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    return headers

def one_page():
    url = 'https://www.229289.com/'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=get_headers(), verify=False)
    print(type(res))
    res.encoding = "UTF-8"
    print(res)
    html = etree.HTML(res.text)
    temp = html.xpath("//div[@class='wshy']/div")
    url_list = []
    for eve in temp:
        url_list.append(''.join(eve.xpath("./div[@class='hyfl']/h3/a/@href")))
    # print(url_list)
    return url_list

one_page()