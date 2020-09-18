# coding: utf-8

import time

def get_params1():
    params1 = {
        'keyword': '家用电器',
        'qrst': '1',
        'wq': '家用电器',
        'stock': '1',
        'page': '2',
        's': '26',
        'scrolling': 'y',
        'log_id': '1595572824986.8881',
        'tpl': '1_M',
        'isList': '0',
        'show_items': '70778912048,100008494250,100001194383,100009506248,7119942,100000035982,100013045832,100003589915,3953597,100003338876,100006464197,6571612,44628412148,100012013848,100008948264,8942387,100006464205,46952510211,45164695399,100000900594,30830765522,1914356,64092858705,3899679,100011373612,5133517,1419129,100002987735,1069555,11677993862',
    }
    return params1

def get_params2(videoid):
    params2 = {
        'callback': 'jQuery5182645',
        'vid': '%s' % videoid,
        'type': '1',
        'from': '1',
        'appid': '24',
        '_': '%s' % int(round(time.time() * 1000)),
    }
    return params2

def get_params3(goods_id, venderId, cate):
    params3 = {
        'skuId': '%s' % goods_id,
        'area': '22_1930_50945_0',
        'venderId': '%s' % venderId,
        'buyNum': '1',
        'choseSuitSkuIds': '',
        'cat': '%s' % cate,
        'extraParam': '{"originid":"1"}',
        'fqsp': '0',
        'pdpin': '',
        'pduid': '1737556876',
        'ch': '1',
        'callback': 'jQuery851120',
    }
    return params3
