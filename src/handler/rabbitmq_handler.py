import pika

from src.config import settings


class RabbitmqHandler:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.message_data = None
        self._config_queue()

    def _config_queue(self):

        settings.log.info("Configuring consumer")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBITMQ_URL))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=settings.EXCHANGE,
                                      exchange_type=settings.EXCHANGE_TYPE,
                                      passive=False,
                                      durable=True,
                                      auto_delete=False)

        self.channel.queue_declare(queue=settings.QUEUE)
        self.channel.queue_bind(queue=settings.QUEUE,
                                exchange=settings.EXCHANGE,
                                routing_key="hola")

        def callback(ch, method, properties, body):
            # self.channel.basic_ack(delivery_tag=method.delivery_tag)
            settings.log.info("Getting data...")
            self.message_data = body.decode('utf-8')

            self.channel.basic_cancel(consumer_tag=settings.CONSUMER_TAG)
            self.channel.stop_consuming()

        self.channel.basic_consume(queue=settings.QUEUE,
                                   auto_ack=True,
                                   on_message_callback=callback,
                                   consumer_tag=settings.CONSUMER_TAG)

    def basic_consume(self):
        try:
            settings.log.info(' [*] Waiting for messages. To exit press CTRL+C')
            self.channel.start_consuming()
        except:
            settings.log.info("error in consumer")

    def basic_producer(self, exchange, routing_key, body):
        self.channel.basic_publish(exchange=exchange,
                                   routing_key=routing_key,
                                   body=body)
        settings.log.info("done!")

    def get_message(self):
        return self.message_data
