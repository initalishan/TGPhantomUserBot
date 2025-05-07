from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from os import system

class Gen_Session:
    def __init__(self):
        self.api_id = int(input("Enter your api id: "))
        self.api_hash = input("Enter your api hash: ")
        with TelegramClient(StringSession(), self.api_id, self.api_hash) as self.phantom:
            self.phantom.send_message("me", self.phantom.session.save())
            system("clear")
            print("dear phantom user. Your string session successfully generated, Check your account save message. Thank You.")
generate_session = Gen_Session()