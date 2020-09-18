# coding: utf-8


def zone_params():
    params = {
        'access_token': '1b4c64d6e8f111ea8586e6531be0cd82',
        'goms_action': '17.api.site.list',
        'api-version': 'v2',
        'appPlatform': 'android',
        'appVersion': 'v6.1.6',
        'deviceInfo': 'Xiaomi_MI 9_5.1.1_CN',
    }
    return params

def cate_params(site_id):
    params = {
        'access_token': '1b4c64d6e8f111ea8586e6531be0cd82',
        'goms_action': '17.api.market.list',
        'site_id': '%s' % site_id,
        'api-version': 'v2',
        'appPlatform': 'android',
        'appVersion': 'v6.1.6',
        'deviceInfo': 'Xiaomi_MI 9_5.1.1_CN',
    }
    return params

def shop_id_params(market_id, page):
    params = {
        'access_token': '1b4c64d6e8f111ea8586e6531be0cd82',
        'goms_action': '17.api.shop.list',
        'page': '%s' % page,
        'page_size': '100',
        'is_flagship': '1',
        'market_id': '%s' % market_id,
        'api-version': 'v1',
        'appPlatform': 'android',
        'appVersion': 'v6.1.6',
        'deviceInfo': 'Xiaomi_MI 9_5.1.1_CN',
    }
    return params

def detail_params(shop_id):
    params = {
        'access_token': '1b4c64d6e8f111ea8586e6531be0cd82',
        'goms_action': '17.api.shop.detail',
        'id': '%s' % shop_id,
        'page': 'detail',
        'api-version': 'v1',
        'appPlatform': 'android',
        'appVersion': 'v6.1.6',
        'deviceInfo': 'Xiaomi_MI 9_5.1.1_CN',
    }
    return params
