from abc import ABC, abstractmethod
from src.models.Diff import Difference
from src.models.State import State

class DiffStrategy(ABC):
    @abstractmethod
    def get_diff(self, state_a: State, state_b: State) -> Difference:
        pass
