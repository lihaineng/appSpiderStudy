import pymongo
from pymongo.collection import Collection
from motor.motor_asyncio import AsyncIOMotorClient


# class Connect_mongo(object):
#     def __init__(self):
#         self.client = pymongo.MongoClient(host='172.18.113.176', port=27017)
#         print('连接成功')
#         self.db_data = self.client['dou_guo_mei_shi']
#
#     def insert_item(self, item):
#         db_collection = Collection(self.db_data, 'dou_guo_mei_shi_item')
#         db_collection.insert(item)
#         print('存储成功')


# mongo_info = Connect_mongo()


# motor：利用它可以完成异步 MongoDB 存储，加快存储速度


class Connect_async_mongo(object):
    def __init__(self):
        self.client = AsyncIOMotorClient('172.18.113.176', 27017)
        print('异步连接成功')
        self.db_data = self.client['async_mei_shi']

    async def insert_async_item(self, item):
        db_collection = await Collection(self.db_data, 'dou_guo_async_item')
        await db_collection.insert(item)
        print('异步存储成功')


mongo_async_info = Connect_async_mongo()
