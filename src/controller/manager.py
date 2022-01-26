from typing import List, Dict
from dataclasses import dataclass
from src.models.NetworkDevice import NetworkDevice, EmptyDevice, CiscoDevice

class TemplateLoader():
    pass

class ParserLoader():
    pass

@dataclass
class ModuleConfig():
    pass

class ModuleLoader():
    def __init__(self, tl: TemplateLoader, pl: ParserLoader, mc: ModuleConfig):
        pass

class InventoryManager():
    def __init__(self):
        self.devices = {}

    def get_devices(self) -> Dict[str, NetworkDevice]:
        return self.devices

    def get_device(self, hostname: str) -> NetworkDevice:
        return self.devices.get(hostname, EmptyDevice())

    def add_device(self, device: NetworkDevice):
        if device.hostname not in self.devices:
            self.devices[device.hostname] = device

    def clear_inventory(self):
        self.devices = {}

class Controller():
    """Manage InventoryManager and Cases."""
    inventory: InventoryManager

    def __init__(self):
        self.inventory = InventoryManager()

    def setup(self):
        self.inventory.add_device(CiscoDevice(
            hostname="R1", address="192.168.122.10",
            username="cisco",password="cisco",
            secret="cisco",platform="cisco_ios"))

    def main(self):
        self.inventory.add_device(CiscoDevice(
            hostname="R1", address="192.168.122.10",
            username="cisco",password="cisco",
            secret="cisco",platform="cisco_ios"))

    def get_device(self):
        return self.inventory.get_device("R1")

if __name__ == "__main__":
    c = Controller()
    c.setup()
    c.get_device()
