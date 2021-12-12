from abc import ABC, abstractmethod
from dataclasses import field


class AbstractComponent(ABC):
    children: list
    build_target: str

    @property
    @abstractmethod
    def code(self) -> str:
        ...


class Component(AbstractComponent):
    def __init__(self, parent, add: bool = True, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

        if not add:
            return

        self.add(parent)

    def add(self, parent):
        if isinstance(parent, AbstractComponent):
            parent.children.append(self)
        else:
            parent.builder.add_component(self)

    @property
    @abstractmethod
    def code(self) -> str:
        ...
