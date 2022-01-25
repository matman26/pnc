from abc import ABC, abstractmethod
from src.models.Connection import ConnectionStrategy

class NetworkDevice(ABC):
    address:    str
    hostname:   str
    username:   str
    password:   str
    secret:     str
    platform:   str

    @abstractmethod
    def connect(self, strategy: ConnectionStrategy):
        pass

class CiscoDevice(NetworkDevice):
    def connect(self):

