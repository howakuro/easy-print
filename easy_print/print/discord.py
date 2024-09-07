from .print import Print
from pathlib import Path

class Discord(Print):
    def init(self, webhook_url: str):
        self.webhook_url = webhook_url

    def print(self, message: str, image: Path = None):
        pass