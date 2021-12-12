from abc import abstractmethod


class Component:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    @property
    @abstractmethod
    def code(self) -> str:
        ...
