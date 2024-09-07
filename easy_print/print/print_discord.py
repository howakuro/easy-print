from .print import Print
from pathlib import Path
import discord


class PrintDiscord(Print):
    def __init__(self, webhook_url: str, webhook_username: str):
        self.__webhook = discord.SyncWebhook.from_url(webhook_url)
        self.__webhook_username = webhook_username

    def print(self, message: str, image=None):
        self.__webhook.send(
            message, username=self.__webhook_username, file=discord.File(image))
