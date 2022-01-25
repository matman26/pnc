from abc import ABC, abstractmethod
from src.models.Parsing import ParsingStrategy

class ConnectionStrategy(ABC):
    @abstractmethod
    def send_command(self, command : str, ParsingStrategy) -> str:
        pass

    @abstractmethod
    def send_config(self, config : str) -> bool:
        pass


class NetmikoStrategy(ConnectionStrategy):
    def send_command(self):
        pass

    def send_config(self, config : str) -> bool:
        return True
