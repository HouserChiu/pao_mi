'''
直播带货榜
'''
import requests
from lxml import etree
import re

def get_headers():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'gr_user_id=f6ed667d-7f1c-4fc4-baef-abe23ad85fcf; grwng_uid=8100f5cd-82b7-4e3f-bf13-0bfa198ca34e; _ga=GA1.2.599738664.1591869428; token=3c1466103c9d317fd6a0bf84d98a327e89f65a0c4ebb24cbd3b79a68d41b9aa65690a8ba5912905b584f53f45a0860479b336eefe61ee38a9b4aeff661fbbb66b66d7809eacd38bfc6bbffdb32561ae293b85d6a3a4a196faaefe04216e46917daf2e3dbf1cfdfaf%3B%20Max-Age; Hm_lvt_348822e7d440f6b751ed21d40cf5b66d=1591869427,1592183723; a57cc8401368a31b_gr_session_id=94fc5067-397a-4ae3-9634-fb261da3877b; a57cc8401368a31b_gr_session_id_94fc5067-397a-4ae3-9634-fb261da3877b=true; _gid=GA1.2.1236659173.1592183724; Hm_lpvt_348822e7d440f6b751ed21d40cf5b66d=1592183735',
        'Host': 'www.bihukankan.com',
        'If-None-Match': '"154e5-50XDMvVPSAwjttPyYJLqHdmIpXw"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    return headers


def get_one():
    url = 'https://www.bihukankan.com/carrierList/live'
    res = requests.get(url, headers=get_headers()).text
    temp = etree.HTML(res).xpath("//div[@class='contain-body']/div[@class='align item-anchor tab-hover']")
    id_list = []
    for eve in temp:
        url = ''.join(eve.xpath("./div[@class='table-list-2']/a/@href"))
        id = re.search('\/hotList\/(\d+).*?gifshow',url,re.S).group(1)
        id_list.append(id)
    # print(id_list)
    return id_list
# get_one()

def get_two():
    # id_list = get_one()
    # for id in id_list:
    url = 'https://www.bihukankan.com/hotList/6518150207270686720/fans?road=gifshow'
        # url = 'https://www.bihukankan.com/hotList/{}/fans?road=gifshow'.format(id)
    temp = requests.get(url, headers=get_headers()).text
    name = ''.join(etree.HTML(temp).xpath("//div[@class='author-name']/text()")).strip()
    account = ''.join(etree.HTML(temp).xpath("//div[@class='aline']/span/text()")).split(':')[1]
    sex = ''.join(etree.HTML(temp).xpath("//div[@class='author-sex-text'][1]/text()"))
    star = ''.join(etree.HTML(temp).xpath("//div[@class='author-sex-text'][2]/text()"))
    location = ''.join(etree.HTML(temp).xpath("//div[@class='author-sex-text'][3]/text()"))
    signature = ''.join(etree.HTML(temp).xpath("//div[@class='author-sex-text oneLine']/text()"))
    fans = ''.join(etree.HTML(temp).xpath("//div[@class='left-data-data number-font none-info']/text()")).split('万')[0].strip()
    production = ''.join(etree.HTML(temp).xpath("//div[@class='left-data-data number-font none-info']/text()")).split('万')[1].strip()
    avatar = ''.join(etree.HTML(temp).xpath("//div[@class='author-icon-contain']/img/@src"))
    province = etree.HTML(temp).xpath("//div[@class='location-list']/div[@class='aline jus ']")
    eve_list = []
    for temp in province:
        province_info = {}
        province_info['province'] = ''.join(temp.xpath("./div[@class='location-name']/text()"))
        province_info['rate'] = ''.join(temp.xpath("./div[@class='item-percent-number number-font']/text()"))
        # eve_list.append(eve)
        print(province_info)
    # print(eve_list)




get_two()

