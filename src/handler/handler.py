from src.services.extract.extract import ExtractAgent
from src.handler.rabbitmq_handler import RabbitmqHandler


class Handler:
    def __init__(self):
        self.extract_obj = ExtractAgent()
        self.mapping = {'extract_all': self.extract_all_handler}
        self.rabbit_handler = RabbitmqHandler()

    def extract_all_handler(self):
        dt = self.extract_obj.extract_by_plugin()
        print(dt)
        # Transform(x)
        # Load(x)

    def execute(self):
        self.rabbit_handler.basic_consume()
        var = self.rabbit_handler.get_message()
        self.mapping[var]()

        self.rabbit_handler.basic_producer(exchange='',
                                           routing_key='orchestrator',
                                           body=b'Done')

        # data =
        # print(data)
