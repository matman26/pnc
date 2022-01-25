from abc import ABC, abstractmethod
from typing import List, Dict
import jinja2

class TemplatingStrategy(ABC):
    @abstractmethod
    def template_string(self, data: List[Dict], template_file: str) -> str:
        pass

class JinjaTemplating(TemplatingStrategy):
    def template_string(self, data: List[Dict], template_file: str) -> str:
        templateEnv = jinja2.Environment()
        template = templateEnv.get_template(template_file)
        return template.render(data=data)
