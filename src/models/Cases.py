from types import ModuleType
from typing import Dict


class ConfigurationCase():
    """Configuration cases are Python modules with
    business logic, parsers, templaters and YANG
    models for interacting with devices and
    providing specific, high-level network services.
    """
    config: Dict

    def __init__(self, module: ModuleType):
        pass
