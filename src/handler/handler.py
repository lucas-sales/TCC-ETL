from src.config import settings
from src.services.extract.extract import ExtractAgent
from src.handler.rabbitmq_handler import RabbitmqHandler
from src.services.transform.trasform_csv import parse_dataframe
from src.services.load.load_data import load


class Handler:
    def __init__(self):
        self.extract_obj = ExtractAgent()
        self.mapping = {'extract_all': self.extract_all_handler}
        self.rabbit_handler = RabbitmqHandler()

    def extract_all_handler(self):
        dt = self.extract_obj.extract_by_plugin()
        parsed_data = parse_dataframe(dt)
        print("Finish!")
        # load(parsed_data)

    def execute(self):
        self.rabbit_handler.basic_consume()
        var = self.rabbit_handler.get_message()
        self.mapping[var]()

        self.rabbit_handler.basic_producer(exchange=settings.EXCHANGE_RESPONSE,
                                           routing_key=settings.QUEUE_ETL_RESPONSE_ROUTING_KEY,
                                           body=b'Done')
