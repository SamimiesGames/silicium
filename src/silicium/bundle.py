from abc import ABC, abstractmethod

from dataclasses import dataclass
from typing import Union

from component import Component


@dataclass
class Bundler(ABC):
    build_component: Union[None, Component]
    components: list[Component]

    @abstractmethod
    def bundle(self) -> str:
        ...
