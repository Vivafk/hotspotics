from telethon import TelegramClient
from pers_data import *

client = TelegramClient('Я устал', api_id, api_hash)

async def main():
    me = await client.get_me()

with client:
    client.loop.run_until_complete(main())