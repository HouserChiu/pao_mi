# coding: utf-8

import time
import urllib.parse

def get_params1(goods_id):
    params1 = {
        'isUseInventoryCenter': 'false',
        'cartEnable': 'true',
        'service3C': 'true',
        'isApparel': 'false',
        'isSecKill': 'false',
        'tmallBuySupport': 'true',
        'isAreaSell': 'false',
        'tryBeforeBuy': 'false',
        'offlineShop': 'false',
        'itemId': '%s' % goods_id,
        'showShopProm': 'false',
        'isPurchaseMallPage': 'false',
        'itemGmtModified': '1595365357000',
        'isRegionLevel': 'false',
        'household': 'false',
        'sellerPreview': 'false',
        'queryMemberRight': 'true',
        'addressLevel': '4',
        'isForbidBuyItem': 'false',
        'callback': 'setMdskip',
        'timestamp': '%s' % int(round(time.time() * 1000)),
        'isg': 'eBgEr4XeONpsdemdBO5aourza7796IRb8sPzaNbMiInca1kf9eOFFNQqEa-eWdtjgt5xmetrA42DhRneSz438PkDBeYCKXIpBjv68e1..',
        'isg2': 'BKioBitmY1w_Rk_ZyVK73OV0eZa60Qzbvi-g4WLZBCMQvUknCuKNai88sVVNjcSz',
        'ref': 'https://s.taobao.com/search?spm=a21bo.2017.201867-links-3.53.14a711d9DzC989&q=%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200420&ie=utf8',
    }
    return params1

def get_params2(pre_cate, i):
    params2 = {
        'data-key': 's',
        'data-value': '176',
        'ajax': 'true',
        '_ksTS': '1595555610867_1239',
        'callback': 'jsonp1240',
        'spm': 'a21bo.2017.201867-links-1.3.3a8011d9Ne0n1P',
        'q': '%s' % pre_cate,
        'imgfile': '',
        'js': '1',
        'stats_click': 'search_radio_all%3A1',
        'initiative_id': 'staobaoz_20190320',
        'ie': 'utf8',
        'bcoffset': '%s' % (-6+int(i)*7),
        'ntoffset': '%s' % (int(i)*7),
        'p4ppushleft': '1%2C48',
        's': '132',
    }
    return params2