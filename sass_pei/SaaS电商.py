# todo: SaaS电商商品上传
# coding=utf-8
# Author: tester_pei
import datetime
import json
import random
from urllib import parse
import requests
from saas_shop.get_goods_info.goods_info_ocalhost import get_goods_info

# 环境配置
from 操作富文本 import format_html, get_html_content
goods_info_path = r'F:\SaaS电商爬取数据'
goods_info_data = get_goods_info(goods_info_path)
# HOST = 'http://118.89.103.186:8062/'  # 测试环境
HOST = 'https://business-api.mydeershow.com'  # 正式环境
# data = {"userLoginName": "13678120001",
#         "code": "862458",
#         "userPassword": "123456aa",
#         "type": "0"}
data = {"userLoginName": "15100000001",
        "code": "862458",
        "userPassword": "123456aa",
        "type": "0"}
headers = {}
data_one = {}
# 获取后台权限
loginApi = parse.urljoin(HOST, 'login')
re_loginApi = requests.request('post', url=loginApi, data=data)
re_loginApi.raise_for_status()
userAuthorization = re_loginApi.json()['returnData']['authorization']
headers['Authorization'] = userAuthorization
print('权限已获取')
# 新建商品
# 第一页数据
# 获取运费
freightSelectApi = parse.urljoin(HOST, '/mgt/mall/product/freightSelect')
re_freightSelectApi = requests.request('post', url=freightSelectApi, headers=headers)
re_freightSelectApi.raise_for_status()
data_one['freightId'] = re_freightSelectApi.json()['returnData'][0]['id']  # 选择第一个运费模板
print('运费模板已获取')
# 获取常用类目
# 获取默认类目
queryCategoriesApi = parse.urljoin(HOST, '/mgt/mall/category/queryCategories')
re_queryCategoriesApi = requests.request('post', url=queryCategoriesApi, headers=headers)
re_queryCategoriesApi.raise_for_status()
# print(re_queryCategoriesApi.json())
# 获取1级类目
oneCategoryApi = parse.urljoin(HOST, '/mgt/mall/category/queryCategoryDefault')
re_oneCategoryApi = requests.request('post', url=oneCategoryApi, headers=headers)
re_oneCategoryApi.raise_for_status()
# print(re_oneCategoryApi.json())
data_one['productCategoryId'] = re_oneCategoryApi.json()['returnData']['categoryId']  # 1级类目
# 获取2级类目
twoCategoryApi = parse.urljoin(HOST, '/mgt/mall/category/findParentId')
two_data = {"parentId": data_one['productCategoryId'],
            "level": 2}
re_twoCategoryApi = requests.request('post', url=twoCategoryApi, data=two_data, headers=headers)
re_twoCategoryApi.raise_for_status()
# print(re_twoCategoryApi.json())
data_one['primaryClassification'] = re_twoCategoryApi.json()['returnData'][0]['id']  # 默认获取第一个2级类目
# 获取3级类目
threeCategoryApi = parse.urljoin(HOST, '/mgt/mall/category/findParentId')
three_data = {"parentId": data_one['primaryClassification'],
              "level": 3}
threeCategoryApi = requests.request('post', url=threeCategoryApi, data=three_data, headers=headers)
threeCategoryApi.raise_for_status()
# print(threeCategoryApi.json())
data_one['secondaryClassification'] = threeCategoryApi.json()['returnData'][0]['id']  # 默认获取第一个3级类目
for goods in goods_info_data:
    # 商品名称
    goods_name = [name for name in goods.keys()][0]
    time = datetime.datetime.now().strftime('%Y_%m_%d')
    data_one['name'] = '更新时间:' + time + '饭团今日爆款!货号:' + goods_name
    # 获取文案
    goods_txt_path = goods[goods_name]['goodsInfo']['info']
    with open(goods_txt_path, 'r', encoding='UTF-8') as f:
        goods_txt = json.load(f)
    # 商品最低价格
    data_one['price'] = goods_txt['data']['get_price'] * 1.25
    # 商品市场价
    data_one['marketPrice'] = goods_txt['data']['get_price'] * 1.5
    # 商品图片
    imgs_list = goods[goods_name]['goodsImg']['imgs']
    imageReqList = []
    img_for_html = []
    for i in imgs_list:
        url = parse.urljoin(HOST, 'uploadImgActivity')
        files = {'file': open(i, 'rb')}
        r = requests.request('post', url=url, headers=headers, files=files, timeout=60)
        r.raise_for_status()
        data = {"url": r.json()['returnData'][0]['fileAllUrl'],
                "resType": 1}
        imageReqList.append(data)
        imgUrl = r.json()['returnData'][0]['fileAllUrl']
        img_for_html.append(imgUrl)
    data_one['imageReqList'] = imageReqList
    # 商品视频
    data_one['videoUrl'] = ''
    # 商品已售数量
    data_one['sales'] = ''  # 空默认为0
    print("第一页请求数据:\n", data_one)
    onePageInsertProductApi = parse.urljoin(HOST, '/mgt/mall/product/insertProduct')
    re_onePageInsertProductApi = requests.request('post', url=onePageInsertProductApi, json=data_one, headers=headers)
    re_onePageInsertProductApi.raise_for_status()
    # print(re_onePageInsertProductApi.json())
    # print("完成第一页数据")
    # 第二页数据
    # 统一规格
    data_two_list = []
    data_two = {}
    # 成本价
    data_two['costPrice'] = goods_txt['data']['get_price']
    # 实际销售价
    data_two['price'] = goods_txt['data']['get_price'] * 1.25
    # 市场价
    data_two['marketPrice'] = goods_txt['data']['get_price'] * 1.5
    # 库存
    data_two['stock'] = '20'
    # 重量
    data_two['weight'] = '0'  # 不超过小数点两位
    # 体积
    data_two['volume'] = '0'  # 不超过小数点两位
    # 商品id-->依赖第一页接口响应
    productId = re_onePageInsertProductApi.json()['returnData']['id']
    data_two['productId'] = productId
    # 规格id-->单独请求
    queryProSpeItemsApi = parse.urljoin(HOST, '/mgt/mall/productSpecItem/queryProSpeItems')
    queryProSpeItemsApi_data = {"productId": productId,
                                "pageNum": 1,
                                "pageSize": 10,
                                "type": 1}
    re_queryProSpeItemsApi = requests.request('post', url=queryProSpeItemsApi, data=queryProSpeItemsApi_data,
                                              headers=headers)
    re_queryProSpeItemsApi.raise_for_status()
    # print(re_queryProSpeItemsApi.json())
    ProSpeItemsId = re_queryProSpeItemsApi.json()['returnData']['data'][0]['id']
    data_two['id'] = ProSpeItemsId
    # 第二页传入参数以列表形式传入
    data_two_list.append(data_two)
    print("第二页请求数据:\n", data_two_list)
    twoUpdateProductSpecItemApi = parse.urljoin(HOST, '/mgt/mall/productSpecItem/updateProductSpecItem')
    re_twoUpdateProductSpecItemApi = requests.request('post', url=twoUpdateProductSpecItemApi, json=data_two_list,
                                                      headers=headers)
    re_twoUpdateProductSpecItemApi.raise_for_status()
    # print(re_twoUpdateProductSpecItemApi.json())
    # 第三页数据
    data_three = {}
    data_three['id'] = productId  # 商品id-->第一步返回的productId
    specialTip = get_html_content(r'D:\Users\cd-2-1\PycharmProjects\test\购买须知.html')
    data_three['specialTip'] = specialTip  # 富文本-->购买须知
    htmlFilePath = r'D:\Users\cd-2-1\PycharmProjects\test\商品富文本模板.html'
    saveHtmlFilePath = f"f:\\htmls\\{goods_name}.html"
    imgs = img_for_html
    data_three['productInfo'] = format_html(htmlFilePath, saveHtmlFilePath, imgs)  # 富文本-->商品详情
    print("第三页请求数据:\n", data_three)
    threeUpdateProductApi = parse.urljoin(HOST, '/mgt/mall/product/updateProduct')
    re_threeUpdateProductApi = requests.request('post', url=threeUpdateProductApi, json=data_three, headers=headers)
    re_threeUpdateProductApi.raise_for_status()
    # print(re_threeUpdateProductApi.json())
    # 商品上架自营店
    startUsingApi = parse.urljoin(HOST, '/mgt/mall/product/startUsing')
    startUsingApi_data = [re_threeUpdateProductApi.json()['returnData']['id']]
    re_startUsingApi = requests.request('post', url=startUsingApi, headers=headers, json=startUsingApi_data)
    re_startUsingApi.raise_for_status()
    # print(re_startUsingApi.json())
    # 将商品添加至共享货架
    settingSupplierChooseGoodsApi = parse.urljoin(HOST,
                                                  '/mgt/mall/supplier/chooseGood/relations/settingSupplierChooseGoods')
    settingSupplierChooseGoodsApi_data = {"reqList": [{"productId": productId}]}
    re_settingSupplierChooseGoodsApi = requests.request('post', url=settingSupplierChooseGoodsApi, headers=headers,
                                                        json=settingSupplierChooseGoodsApi_data)
    re_settingSupplierChooseGoodsApi.raise_for_status()
    # print(re_settingSupplierChooseGoodsApi.json())
    # 查询商品规格id用于设置利润率
    itemPageQueryApi = parse.urljoin(HOST, '/mgt/mall/supplier/chooseGood/relations/item/pageQuery')
    itemPageQueryApi_data = {"pageNum": 1,
                             "pageSize": 5000,
                             "productId": productId}
    re_itemPageQueryApi = requests.request('post', url=itemPageQueryApi, json=itemPageQueryApi_data, headers=headers)
    re_itemPageQueryApi.raise_for_status()
    # print(re_itemPageQueryApi.json())
    # 设置利润率
    # b = random.randint(1, 50)
    updateProfitMarginApi = parse.urljoin(HOST, '/mgt/mall/supplier/chooseGood/relations/item/updateProfitMargin')
    # updateProfitMarginApi_data = {"ids": [re_itemPageQueryApi.json()['returnData'][0]['id']],
    #                               "profitMargin": b/100}  # 设置利润率范围0.01~0.5
    updateProfitMarginApi_data = {"ids": [re_itemPageQueryApi.json()['returnData'][0]['id']],
                                  "profitMargin": 0.1}  # 设置利润率范围0.01~0.5
    print(updateProfitMarginApi_data)
    re_updateProfitMarginApi = requests.request('post', url=updateProfitMarginApi, json=updateProfitMarginApi_data,
                                                headers=headers)
    re_updateProfitMarginApi.raise_for_status()
    # print(re_updateProfitMarginApi.json())
    # 将设置好利润率的商品进行上架
    # 查询共享货架商品id
    relationsPageQueryApi = parse.urljoin(HOST, '/mgt/mall/supplier/chooseGood/relations/pageQuery')
    relationsPageQueryApi_data = {"productName": "",
                                  "pageNum": 1,
                                  "pageSize": 10,
                                  "kindId": ""}
    re_relationsPageQueryApi = requests.request('post', url=relationsPageQueryApi, json=relationsPageQueryApi_data,
                                                headers=headers)
    re_relationsPageQueryApi.raise_for_status()
    # print(re_relationsPageQueryApi.json())
    # 上架
    enableOrDisableSupplierChooseGoodsApi = parse.urljoin(HOST, '/mgt/mall/supplier/chooseGood/relations'
                                                                '/enableOrDisableSupplierChooseGoods')
    enableOrDisableSupplierChooseGoodsApi_data = {"id": re_relationsPageQueryApi.json()['returnData'][0]['id'],
                                                  "isEnable": "true"}
    re_enableOrDisableSupplierChooseGoodsApi = requests.request('post', url=enableOrDisableSupplierChooseGoodsApi,
                                                                json=enableOrDisableSupplierChooseGoodsApi_data,
                                                                headers=headers)
    re_enableOrDisableSupplierChooseGoodsApi.raise_for_status()
    print(re_enableOrDisableSupplierChooseGoodsApi.json())
