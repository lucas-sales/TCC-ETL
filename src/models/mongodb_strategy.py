from abc import ABC, abstractmethod


class MongodbStrategy(ABC):
    @abstractmethod
    def connection(self):
        pass

    @abstractmethod
    def save_many(self, data, collection_name):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_collection(self):
        pass

    @abstractmethod
    def get_document(self):
        pass

    @abstractmethod
    def drop_collection(self, collection):
        pass

    @abstractmethod
    def close(self):
        pass
