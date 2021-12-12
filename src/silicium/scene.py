from dataclasses import dataclass

from abc import ABC

from .builder import AbstractBuilder


@dataclass
class AbstractScene(ABC):
    builder: AbstractBuilder
