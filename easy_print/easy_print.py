from pathlib import Path
from .print import Print

class EasyPrint:
    def __init__(self, print_class_list: Print = None):
        self.print_class_list: list[Print]  = print_class_list
    
    def print(self, message: str, image: Path = None):
        for print_class in self.print_class_list:
            print_class.print(message, image)