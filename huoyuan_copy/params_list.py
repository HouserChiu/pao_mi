# coding: utf-8


def zone_params():
    params = {
        'access_token': '20e3f2c5ee7911eab61f5262861debda',
        'goms_action': '17.api.site.list',
        'api-version': 'v2',
        'appPlatform': 'android',
        'appVersion': 'v6.1.6',
        'deviceInfo': 'Xiaomi_MI 9_5.1.1_CN',
    }
    return params

def cate_params():
    params = {
        'access_token': '20e3f2c5ee7911eab61f5262861debda',
        'goms_action': '17.api.market.list',
        'site_id': '28',
        'api-version': 'v2',
        'appPlatform': 'android',
        'appVersion': 'v6.1.6',
        'deviceInfo': 'Xiaomi_MI 9_5.1.1_CN',
    }
    return params

def shop_id_params(market_id, page):
    params = {
        'access_token': '20e3f2c5ee7911eab61f5262861debda',
        'goms_action': '17.api.shop.list',
        'site_id': '28',
        'market_id': '%s' % market_id,
        'page': '%s' % page,
        'page_size': '20',
        'sort': 'floor-id',
        'api-version': 'v1',
        'appPlatform': 'android',
        'appVersion': 'v6.1.6',
        'deviceInfo': 'Xiaomi_MI 9_5.1.1_CN',
    }
    return params

def detail_params(shop_id):
    params = {
        'access_token': '20e3f2c5ee7911eab61f5262861debda',
        'goms_action': '17.api.shop.detail',
        'id': '%s' % shop_id,
        'page': 'detail',
        'api-version': 'v1',
        'appPlatform': 'android',
        'appVersion': 'v6.1.6',
        'deviceInfo': 'Xiaomi_MI 9_5.1.1_CN',
    }
    return params
