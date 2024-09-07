from abc import ABCMeta, abstractmethod
from pathlib import Path


class Print(metaclass=ABCMeta):
    @abstractmethod
    def print(self, message: str, image=None):
        pass
