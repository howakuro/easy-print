import os
import unittest
import easy_print
import sys
import dotenv
from tests.util_test import stub_stdouts, stub_stdin
from pathlib import Path

dotenv.load_dotenv("../.env")


class EasyPrintTest(unittest.TestCase):
    TEST_DATA: str = "testTesttestTest"
    IMAGE_PATH: Path = Path(__file__).parent.joinpath(
        "testdata/test_image.png")

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
        mock_list = [MockPrint(), MockPrint(), MockPrint()]
        test = easy_print.EasyPrint(mock_list)
        test.print(self.TEST_DATA)

        for mock in mock_list:
            self.assertEqual(mock.message, self.TEST_DATA)

    def test_stdio(self):
        """
        StdIOクラスが正常に動くことを検証する
        """
        stub_stdouts(self)

        mock = easy_print.PrintStdIO()
        test = easy_print.EasyPrint([mock])
        test.print(self.TEST_DATA)

        self.assertEqual(sys.stdout.getvalue(), self.TEST_DATA+"\n")

    def test_discord(self):
        """
        Discordクラスが正常に動くことを検証する
        """
        DISCORD_WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
        USER_NAME = "webhook_test2"

        mock = easy_print.PrintDiscord(DISCORD_WEBHOOK_URL, USER_NAME)
        test = easy_print.EasyPrint([mock])
        with open(self.IMAGE_PATH, "rb") as image_file:
            test.print(self.TEST_DATA, image=image_file)

    def test_line_notify(self):
        """
        LineNotifyクラスが正常に動くことを検証する
        """
        LINE_NOTIFY_TOKEN = os.environ["LINE_NOTIFY_TOKEN"]

        mock = easy_print.PrintLineNotify(LINE_NOTIFY_TOKEN)
        test = easy_print.EasyPrint([mock])
        with open(self.IMAGE_PATH, "rb") as image_file:
            test.print(self.TEST_DATA, image=image_file)


class MockPrint(easy_print.Print):
    def print(self, message: str, image: Path = None):
        self.message = message
        self.image = image
