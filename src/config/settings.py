import logging
import os

from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(format="%(asctime)s |%(name)s| %(levelname)s: %(message)s", level=logging.INFO)
log = logging.getLogger(__name__)

# APP
CSV_FILE_PATH = os.environ.get('CSV_FILE_PATH')
PLUGIN = os.environ.get('PLUGIN')

# Rabbitmq
RABBITMQ_URL = os.environ.get('RABBITMQ_URL')
EXCHANGE = os.environ.get('EXCHANGE')
EXCHANGE_RESPONSE = os.environ.get('EXCHANGE_RESPONSE')
EXCHANGE_TYPE = os.environ.get('EXCHANGE_TYPE')

QUEUE_ETL = os.environ.get('QUEUE_ETL')
QUEUE_RESPONSE = os.environ.get('QUEUE_RESPONSE')
QUEUE_RESPONSE_ROUTING_KEY = os.environ.get('QUEUE_RESPONSE_ROUTING_KEY')

CONSUMER_TAG = os.environ.get('CONSUMER_TAG')

# MONGO
MONGODB_URL = os.environ.get('MONGODB_URL')
MONGODB_DATABASE = os.environ.get('MONGODB_DATABASE')
MONGODB_COLLECTION = os.environ.get('MONGODB_COLLECTION')


def load():
    log.info('Loading settings...')
    required_env_vars = [
        'CSV_FILE_PATH',
        'PLUGIN',
        'RABBITMQ_URL',
        'EXCHANGE',
        'EXCHANGE_RESPONSE',
        'EXCHANGE_TYPE',
        'QUEUE_ETL',
        'CONSUMER_TAG',
        'MONGODB_URL',
        'MONGODB_DATABASE',
        'MONGODB_COLLECTION',
        'QUEUE_RESPONSE',
        'QUEUE_RESPONSE_ROUTING_KEY'
    ]

    for env_var in required_env_vars:
        if env_var not in os.environ:
            raise EnvironmentError(f'Environment variable not founded.')
