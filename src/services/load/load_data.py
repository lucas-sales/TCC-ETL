from src.repository.mongodb_repository import MongoDBRepository
from src.config import settings


def load(data: list):
    mongo = MongoDBRepository(settings.MONGODB_URL, settings.MONGODB_DATABASE)
    mongo.connection()
    mongo.save_many(data, settings.MONGODB_COLLECTION)
