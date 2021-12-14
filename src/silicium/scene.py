from dataclasses import dataclass
from abc import ABC, abstractmethod

from .builder import AbstractBuilder


@dataclass
class AbstractScene(ABC):
    builder: AbstractBuilder

    @abstractmethod
    def run(self) -> None:
        ...
