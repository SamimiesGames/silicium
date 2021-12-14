from abc import ABC, abstractmethod

from dataclasses import dataclass, field
# Added list for typing for back compatibility to 3.8 and 3.7
from typing import Union, List

from .component import AbstractComponent


@dataclass
class AbstractBuilder(ABC):
    builder_component: Union[None, AbstractComponent] = None
    # use List instead of list for typehint for py37 and py38
    components: List[AbstractComponent] = field(default_factory=list)

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

