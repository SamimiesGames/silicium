from abc import ABC, abstractmethod

from dataclasses import dataclass, field
from typing import Union

from .component import AbstractComponent


@dataclass
class AbstractBuilder(ABC):
    builder_component: Union[None, AbstractComponent] = None
    components: list[AbstractComponent] = field(default_factory=list)

    @abstractmethod
    def add_component(self, component: AbstractComponent):
        ...

    @abstractmethod
    def build(self, build_content: str = None):
        ...


class Builder(AbstractBuilder):
    def add_component(self, component: AbstractComponent):
        self.components.append(component)

    @abstractmethod
    def build(self, build_content: str = None) -> str:
        ...

