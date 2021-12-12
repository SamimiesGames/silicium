from abc import ABC, abstractmethod
from dataclasses import dataclass

import uuid


@dataclass
class AbstractComponent(ABC):
    build_target: str
    parent: any
    sub_components: list

    @property
    @abstractmethod
    def code(self) -> str:
        ...

    @abstractmethod
    def grand_render(self):
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
            self.parent.sub_components.append(self)
        else:
            self.parent.builder.add_component(self)

    def __repr__(self):
        return f"{self.__class__.__name__}"

    @property
    @abstractmethod
    def code(self) -> str:
        ...

    def grand_render(self) -> str:
        sub_component_index = self.code.rfind("<")
        left_side, right_side = self.code[:sub_component_index], self.code[sub_component_index:]

        sub_component_html = ""

        if self.sub_components:
            for sub_component in self.sub_components:
                sub_component_html += sub_component.grand_render()

        return f"{left_side}{sub_component_html}{right_side}"

