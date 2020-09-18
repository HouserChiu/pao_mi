import requests
from lxml import etree


def get_headers():
    headers = {
        'Referer': 'http://www.wwssr.com/nc/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    return headers


def one_page():
    url_list = []
    url = 'http://www.wwssr.com/'
    html = requests.get(url, headers=get_headers()).text
    temp = etree.HTML(html).xpath("//ul[@class='clearfix']/li")
    for eve in temp:
        eves = eve.xpath("./a/@href")
        url_list.append(eves)
    # print(url_list)
    return url_list


def two_page():
    urlss = one_page()
    wx_list = []
    for urls in urlss:
        for url in urls:
            html = requests.get(url, headers=get_headers()).text
            temp = etree.HTML(html).xpath("//div[@class='count clearfix']/ul/li[2]/span/text()")
            wx_list.append(temp)
    print(wx_list)


two_page()
