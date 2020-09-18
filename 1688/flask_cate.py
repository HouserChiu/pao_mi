# coding: utf-8

'''封装成无参数传入的接口'''
from flask import Flask, jsonify, request
from get_cate_api import get_cate
from get_scan_id_api import get_params
from get_detail_api import get_detail
from get_id import get_id_info

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

# 大类接口
@app.route('/get_cate', methods=['get'])
def get_user():
    data = get_cate()
    return jsonify(data)

# 大类下多个商品的id
@app.route('/get_cate/get_id', methods=['get'])
def get_id():
    cate = request.args.get('cate')
    page = request.args.get('page')
    res = get_id_info(cate, page)
    return jsonify(res)

# 大类下多个商品详情
@app.route('/get_cate/get_id/get_detail', methods=['get'])
def get_one_page():
    cate = request.args.get('cate')
    page = request.args.get('page')
    res = get_params(cate, page)
    return jsonify(res)

# 传入单个id获得对应详细信息
@app.route('/get_cate/get_id/get_one_detail', methods=['get'])
def get_ss():
    username = request.args.get('goods_id')
    res = get_detail(username)
    return jsonify(res)

app.run(host='0.0.0.0', port=8803, debug=True)
