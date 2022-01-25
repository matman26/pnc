from abc import ABC, abstractmethod
from typing import Dict, Any
from ttp import ttp


class ParsingStrategy(ABC):
    @abstractmethod
    def parse_string(self, string: str, template: str) -> Dict[str,Any]:
        pass

class NoParsing(ParsingStrategy):
    def parse_string(self, string: str) -> Dict[str, Any]:
        return {
            "results" : string }

class TTPParsing(ParsingStrategy):
    def parse_string(self, string: str, template: str) -> Dict[str, Any]:
        parser = ttp(data=string, template=template)
        parser.parse()
        return {
            "results": parser.result(format='raw') }
