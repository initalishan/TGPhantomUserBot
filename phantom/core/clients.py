from dotenv import load_dotenv
from telethon import TelegramClient
from pytgcalls import PyTgCalls
from telethon.sessions import StringSession
from os import environ

load_dotenv()
api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
session = environ["STRING_SESSION"]
phantom = TelegramClient(StringSession(session), api_id, api_hash)
phantomCall = PyTgCalls(phantom)
phantomCall.start()