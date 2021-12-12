from abc import ABC, abstractmethod


class AbstractComponent(ABC):
    @property
    @abstractmethod
    def code(self) -> str:
        ...


class Component(AbstractComponent):
    def __init__(self, scene, add_now: bool = True, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

        if add_now:
            scene.builder.add_component(self)

    @property
    @abstractmethod
    def code(self) -> str:
        ...
