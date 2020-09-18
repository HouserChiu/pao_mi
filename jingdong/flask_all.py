# coding: utf-8

from flask import Flask, jsonify, request
from get_cate import cate_info
from get_id import get_id_info
from get_detail import get_detail_info
from get_one_detail import one_detail_info

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

# 大类接口
@app.route('/get_cate', methods=['get'])
def cate_one():
    data = cate_info()
    return jsonify(data)

# 大类下多个商品的id
@app.route('/get_cate/get_id', methods=['get'])
def id_two():
    cate = request.args.get('cate')
    res = get_id_info(cate)
    return jsonify(res)

# 单个类别下多个商品详情
@app.route('/get_cate/get_id/get_detail', methods=['get'])
def detail_three():
    cate = request.args.get('cate')
    res = get_detail_info(cate)
    return jsonify(res)

# 传入id获得单个商品详细信息
@app.route('/get_cate/get_id/get_one_detail', methods=['get'])
def detail_one():
    ids = request.args.get('goods_id')
    res = one_detail_info(ids)
    return jsonify(res)

app.run(host='0.0.0.0', port=8800, debug=True)