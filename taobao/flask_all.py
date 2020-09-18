# coding: utf-8

from flask import Flask, jsonify, request
from get_cate_api import cate_one
from get_detail_api import two_detail
from get_id_api import one_id
from get_one_detail import one_product_detail
from get_cate_api_plus import cate_one_plus
from get_id_api_plus import one_id_plus

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

# 大类接口
@app.route('/get_cate', methods=['get'])
def flask_cate():
    data = cate_one()
    return jsonify(data)

# 大类接口plus
@app.route('/get_cate_plus', methods=['get'])
def flask_cate_plus():
    data = cate_one_plus()
    return jsonify(data)

# 大类下多个商品详情
@app.route('/get_cate/one_page', methods=['get'])
def get_two_page():
    cate = request.args.get('cate')
    res = two_detail(cate)
    return jsonify(res)

# 大类下多个商品的id
@app.route('/get_cate/get_id', methods=['get'])
def get_one_page():
    cate = request.args.get('cate')
    res = one_id(cate)
    return jsonify(res)

# 大类下多个商品的id (plus)
@app.route('/get_cate/get_id_plus', methods=['get'])
def get_one_page_plus():
    cate = request.args.get('cate')
    i = request.args.get('i')
    res = one_id_plus(cate, i)
    return jsonify(res)

# 传入单个id获得对应详细信息
@app.route('/get_cate/get_id/get_one_detail', methods=['get'])
def get_one_info():
    username = request.args.get('goods_id')
    res = one_product_detail(username)
    return jsonify(res)


app.run(host='0.0.0.0', port=8802, debug=True)

