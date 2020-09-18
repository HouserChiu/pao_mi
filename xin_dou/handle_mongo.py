import pymongo
from pymongo.collection import Collection

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client['douyin']


# 把douyin_hot_id.txt中的id存入到数据库
def handle_init_task():
    # 表名称
    task_id_collection = Collection(db, 'task_id')
    with open('douyin_hot_id.txt', 'r') as f_share:
        # 使用readlines把douyin_hot_id变成列表
        for f_share_task in f_share.readlines():
            init_task = {}
            init_task['share_id'] = f_share_task.replace('\n', '')
            task_id_collection.insert(init_task)


# 取出数据库中的id
def handle_get_task():
    task_id_collection = Collection(db, 'task_id')
    return task_id_collection.find_one_and_delete({})


handle_init_task()
