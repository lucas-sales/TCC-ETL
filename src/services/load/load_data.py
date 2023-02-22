from src.repository.mongodb_repository import MongoDBRepository
from src.config import settings


def load(data: list):
    mongo = MongoDBRepository(settings.MONGODB_URL, settings.MONGODB_DATABASE)
    mongo.connection()
    try:
        mongo.save_many(data[1:1000], settings.MONGODB_COLLECTION)
        settings.log.info(f'Data saved')
    except Exception as e:
        print(e)


