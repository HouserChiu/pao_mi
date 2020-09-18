# coding: utf-8

import pymongo
from pymongo.collection import Collection

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client['cate_info']

# 取出数据库中的cate
def handle_get_task():
    task_id_collection = Collection(db, 'cate_info_data')
    return task_id_collection.find_one_and_delete({})
    # one_cates = task_id_collection.find_one_and_delete({})

    # for one_cate in one_cates:
    #     print(one_cate)

# while True:
#     one_cates = handle_get_task()
#     if one_cates != None:
#         for cate in one_cates['temp']:
#             print(cate)
#     else:
#         break
