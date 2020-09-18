# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from android_one_page import get_cate
from android_two_page import get_id_info
from android_three_page import get_detail




app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"


# 大类接口
@app.route('/get_cate', methods=['get'])
def get_cate_one():
    data = get_cate()
    return jsonify(data)
    # return json.dumps(data, ensure_ascii=False)

# 大类下多个商品的id
@app.route('/get_cate/get_id', methods=['get'])
def get_id():
    cate = request.args.get('cate')
    page = request.args.get('page')
    res = get_id_info(cate, page)
    return jsonify(res)

# 大类下多个商品详情
@app.route('/get_cate/get_id/get_detail', methods=['get'])
def detail():
    cate = request.args.get('cate')
    page = request.args.get('page')
    res = get_detail(cate, page)
    return jsonify(res)


app.run(host='0.0.0.0', port=8801, debug=True)




