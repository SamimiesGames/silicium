from abc import ABC, abstractmethod


class AbstractAction(ABC):
    @abstractmethod
    def on_trigger(self):
        ...

    @abstractmethod
    def on_deploy(self):
        ...
