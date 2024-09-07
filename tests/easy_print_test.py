import unittest
import easy_print
from pathlib import Path

class EasyPrintTest(unittest.TestCase):    
    def test_init(self):
        # 初期化ができることを検証する
        easy_print.EasyPrint()
    
    def test_print(self):
        # printメソッドが正常に動くことを検証する
        mock_list = [MockPrint(), MockPrint(), MockPrint()]
        test_date = "testTesttestTest"
        test = easy_print.EasyPrint(mock_list)
        test.print(test_date)
        
        for mock in mock_list:
            self.assertEqual(mock.message, test_date)
    

class MockPrint(easy_print.Print):
    def print(self, message: str, image: Path = None):
        self.message = message
        self.image = image