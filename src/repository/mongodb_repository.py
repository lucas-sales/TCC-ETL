from abc import ABC

from pymongo import MongoClient

from src.models.mongodb_strategy import MongodbStrategy


class MongoDBRepository(ABC, MongodbStrategy):
    def __init__(self, connection_string: str, database_name: str, ):
        self.connection_string = connection_string
        self.database_name = database_name
        self._client = None
        self._db = None
        self._col = None

    def connection(self):
        self._client = MongoClient(self.connection_string)
        self._db = self._client[self.database_name]

    def save_many(self, data, collection_name):
        self._col = self._db[collection_name]
        x = self._col.insert_many(data)

    def update(self):
        pass

    def get_collection(self):
        pass

    def get_document(self):
        pass

    def drop_collection(self, collection):
        self._col = self._db[collection]
        self._col.drop()

    def close(self) -> None:
        self._client.close()
