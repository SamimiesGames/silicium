from abc import ABC, abstractmethod


class AbstractComponent(ABC):
    build_target: str

    @property
    @abstractmethod
    def code(self) -> str:
        ...


class Component(AbstractComponent):
    def __init__(self, scene, add: bool = True, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

        if add:
            scene.builder.add_component(self)

    @property
    @abstractmethod
    def code(self) -> str:
        ...
