from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, PyMongoError
from settings import MONGO_DB_URI, MONGO_DB_DATABASE_NAME

class DatabaseManager:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        try:
            self.client = MongoClient(MONGO_DB_URI)
            self.db = self.client[MONGO_DB_DATABASE_NAME]
            if self.collection_name in self.db.list_collection_names():
                print(f"Collection '{self.collection_name}' already exists. Ready to perform operations.")
            else:
                self.db.create_collection(self.collection_name)
                print(f"Collection '{self.collection_name}' created. Ready to perform operations.")
        except ServerSelectionTimeoutError:
            print("Failed to connect to MongoDB. Please check your URI and network connection.")
        except PyMongoError as e:
            print(f"An error occurred while setting up the database: {e}")

    def insert_one(self, collection_name, document):
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(document)
            return result.inserted_id
        except PyMongoError as e:
            print(f"An error occurred during insertion: {e}")

    def find_one(self, collection_name, query):
        try:
            collection = self.db[collection_name]
            return collection.find_one(query)
        except PyMongoError as e:
            print(f"An error occurred during find operation: {e}")

    def update_one(self, collection_name, query, update):
        try:
            collection = self.db[collection_name]
            result = collection.update_one(query, {'$set': update})
            return result.modified_count
        except PyMongoError as e:
            print(f"An error occurred during update operation: {e}")

    def delete_one(self, collection_name, query):
        try:
            collection = self.db[collection_name]
            result = collection.delete_one(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"An error occurred during deletion: {e}")

    def close(self):
        """Close the MongoDB connection."""
        if hasattr(self, 'client') and self.client is not None:
            self.client.close()
            print("MongoDB connection closed.")

# Example usage:
# db_manager = DatabaseManager('my_collection')
# db_manager.insert_one('my_collection', {'name': 'Alice'})
# db_manager.close()
