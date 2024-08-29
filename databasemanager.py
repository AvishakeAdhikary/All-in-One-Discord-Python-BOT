from pymongo import MongoClient
from pymongo.errors import ConnectionError
from settings import MONGO_DB_URI, MONGO_DB_DATABASE_NAME, MONGO_DB_COLLECTION_NAME

class DatabaseManager:
    def __init__(self):
        try:
            self.client = MongoClient(MONGO_DB_URI)
            self.db = self.client[MONGO_DB_DATABASE_NAME]
            self.collection_name = MONGO_DB_COLLECTION_NAME
            if self.collection_name in self.db.list_collection_names():
                print(f"Collection '{self.collection_name}' already exists.")
            else:
                self.db.create_collection(self.collection_name)
                print(f"Collection '{self.collection_name}' created.")
        except ConnectionError:
            print("Failed to connect to MongoDB. Please check your URI and network connection.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.client.close()

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
