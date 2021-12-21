from abc import ABC, abstractmethod
from dataclasses import dataclass

import uuid


@dataclass
class AbstractComponent(ABC):
    build_target: str
    parent: any
    absolute_root: any
    sub_components: list

    @property
    @abstractmethod
    def code(self) -> str:
        ...


class Component(AbstractComponent):
    def __init__(self, parent, add: bool = True, **kwargs):
        self.parent = parent
        self.sub_components = []

        self.id = uuid.uuid4()

        for name, value in kwargs.items():
            setattr(self, name, value)

        if not add:
            return

        if isinstance(self.parent, AbstractComponent):
            self.absolute_root = self.parent.absolute_root
            self.parent.sub_components.append(self)
        else:
            self.absolute_root = self.parent
            self.parent.builder.add_component(self)

    def __repr__(self):
        return f"{self.__class__.__name__}"

    @property
    @abstractmethod
    def code(self) -> str:
        ...
