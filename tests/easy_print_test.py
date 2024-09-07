import unittest
import easy_print
import sys
from util_test import stub_stdouts, stub_stdin
from pathlib import Path

class EasyPrintTest(unittest.TestCase):    
    def test_init(self):
        """
        初期化ができることを検証する
        """
        # 初期化ができることを検証する
        easy_print.EasyPrint()

    def test_print(self):
        """
        printメソッドが正常に動くことを検証する
        """
        test_date = "testTesttestTest"
        
        mock_list = [MockPrint(), MockPrint(), MockPrint()]
        test = easy_print.EasyPrint(mock_list)
        test.print(test_date)
        
        for mock in mock_list:
            self.assertEqual(mock.message, test_date)

    def test_stdio(self):
        """
        StdIOクラスが正常に動くことを検証する
        """
        stub_stdouts(self)
        test_date = "testTesttestTest"
        
        mock = easy_print.StdIO()
        test = easy_print.EasyPrint([mock])
        test.print(test_date)
        
        self.assertEqual(sys.stdout.getvalue(), test_date+"\n")


class MockPrint(easy_print.Print):
    def print(self, message: str, image: Path = None):
        self.message = message
        self.image = image