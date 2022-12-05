from abc import ABC, abstractmethod


class HandlerStrategy(ABC):
    @abstractmethod
    def extract_all_handler(self):
        pass

    @abstractmethod
    def execute(self):
        pass
