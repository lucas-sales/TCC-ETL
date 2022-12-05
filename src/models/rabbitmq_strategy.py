from abc import ABC, abstractmethod


class RabbitmqStrategy(ABC):
    @abstractmethod
    def _config_queue(self):
        pass

    @abstractmethod
    def basic_consume(self):
        pass

    @abstractmethod
    def basic_producer(self, exchange: str, routing_key: str, body: bytes):
        pass

    @abstractmethod
    def get_message(self):
        pass
