from .print import Print
from pathlib import Path
import requests


class PrintLineNotify(Print):
    NOTIFY_API_URL: str = "https://notify-api.line.me/api/notify"

    def __init__(self, token: str):
        self.token = token

    def print(self, message: str, image=None):
        headers = {"Authorization": "Bearer " + self.token}
        files = None
        payload = {"message": message}

        if image is not None:
            files = {"imageFile": image}

        requests.post(self.NOTIFY_API_URL, headers=headers,
                      params=payload, files=files)
