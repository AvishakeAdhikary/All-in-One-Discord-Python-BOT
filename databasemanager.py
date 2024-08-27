from pymongo import MongoClient
from settings import MONGO_DB_URI, MONGO_DB_DATABASE_NAME

class DatabaseManager:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[MONGO_DB_DATABASE_NAME]

    def insert_one(self, collection_name, document):
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id

    def find_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def update_one(self, collection_name, query, update):
        collection = self.db[collection_name]
        return collection.update_one(query, {'$set': update})

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)
