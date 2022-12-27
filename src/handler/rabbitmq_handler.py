from abc import ABC

import pika

from src.config import settings
from src.models.rabbitmq_strategy import RabbitmqStrategy


class RabbitmqHandler(RabbitmqStrategy, ABC):
    def __init__(self):
        self.connection = None
        self.channel = None
        self.message_data = None
        self._config_queue()

    def _config_queue(self):

        settings.log.info("Configuring consumer")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBITMQ_URL))
        self.channel = self.connection.channel()

        def callback(ch, method, properties, body):
            # self.channel.basic_ack(delivery_tag=method.delivery_tag)
            settings.log.info("Getting data...")
            self.message_data = body.decode('utf-8')

            self.channel.basic_cancel(consumer_tag=settings.CONSUMER_TAG)
            self.channel.stop_consuming()

        self.channel.basic_consume(queue=settings.QUEUE_ETL,
                                   auto_ack=True,
                                   on_message_callback=callback,
                                   consumer_tag=settings.CONSUMER_TAG)

    def basic_consume(self):
        try:
            settings.log.info(' [*] Waiting for messages. To exit press CTRL+C')
            self.channel.start_consuming()
        except Exception as e:
            settings.log.info(f'error in consumer: {e}')

    def basic_producer(self, exchange: str, routing_key: str, body: bytes):
        self.channel.basic_publish(exchange=exchange,
                                   routing_key=routing_key,
                                   body=body)
        settings.log.info("done!")

    def get_message(self):
        return self.message_data
