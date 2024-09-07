from .print import Print
from pathlib import Path


class PrintStdIO(Print):
    def print(self, message: str, image=None):
        """
        NOTE: 標準入出力は画像出力に対応していません
        """
        print(message)
