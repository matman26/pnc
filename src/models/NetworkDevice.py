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

class EmptyDevice(NetworkDevice):
    def connect(self, strategy: ConnectionStrategy):
        pass

class CiscoDevice(NetworkDevice):
    def __init__(self, address, hostname, username, password,
                 secret, platform):
        self.address  = address
        self.hostname = hostname
        self.username = username
        self.password = password
        self.secret   = secret
        self.platform = platform

    def connect(self):
        pass

