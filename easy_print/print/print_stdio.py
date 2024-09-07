from .print import Print
from pathlib import Path


class PrintStdIO(Print):
    def print(self, message: str, image=None):
        """
        標準出力にメッセージを出力します

        Parameters
        ----------
        message : str
            出力するメッセージ
        image : Path
            画像を出力するにはこのパスを指定してください
            ただし、標準入出力は画像出力に対応していません
        """

        """
        NOTE: 標準入出力は画像出力に対応していません
        """
        print(message)
