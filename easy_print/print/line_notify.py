from .print import Print
from pathlib import Path

class LIneNotify(Print):
    def __init__(self, token: str):
        self.token = token

    def print(self, message: str, image: Path = None):
        pass