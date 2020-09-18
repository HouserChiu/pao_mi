# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from get_cate_api import get_cate
from get_one_page import one_page
from one_product_detail import one_detail

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"


# 大类接口
@app.route('/get_cate', methods=['get'])
def get_cate_one():
    data = get_cate()
    return jsonify(data)


# 大类下多个商品的id
@app.route('/get_cate/get_id', methods=['get'])
def get_id():
    cate = request.args.get('cate')
    page = request.args.get('page')
    res = one_page(cate, page)
    return jsonify(res)


# 大类下单个商品详情
@app.route('/get_cate/get_id/get_one_detail', methods=['get'])
def detail():
    goods_id = request.args.get('goods_id')
    res = one_detail(goods_id)
    return jsonify(res)


app.run(host='0.0.0.0', port=8804, debug=True)
