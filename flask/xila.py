import requests
from lxml import etree
def craw():
    res = requests.get('http://www.xiladaili.com/').text
    temp = etree.HTML(res)
    pros = temp.xpath("//table[@class='fl-table']/tbody/tr")
    item = []
    for pro in pros:
        info = {}
        info['eve'] = pro.xpath("./td[1]/text()")
        item.append(info['eve'])
    return item
