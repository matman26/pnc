from typing import List
from src.models.NetworkDevice import NetworkDevice, EmptyDevice, CiscoDevice

class InventoryManager():
    def __init__(self):
        self.devices = []

    def get_devices(self) -> List[NetworkDevice]:
        return self.devices

    def get_device(self, hostname: str) -> NetworkDevice:
        out_device = EmptyDevice()
        for index, device in enumerate(self.devices):
            if device.hostname == hostname:
                out_device = self.devices[index]
        return out_device

    def add_device(self, device: NetworkDevice):
        if device not in self.devices:
            self.devices.append(device)

    def clear_inventory(self):
        self.devices = []

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
