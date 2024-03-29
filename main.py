from telethon.sync import TelegramClient
from pers_data import *
import json

client = TelegramClient(username, api_id, api_hash)
client.start()

# Идентификатор канала, из которого хотите скачать посты
channel_username = 'https://t.me/bdufstecru'
channel_entity = client.get_entity(channel_username)

# Скачивание постов и сохранение в файл JSON
posts = client.get_messages(channel_entity, limit=10)  # Указать нужное количество постов
posts_json = [post.to_dict() for post in posts]
with open('posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts_json, f, ensure_ascii=False, indent=4)

# Закрытие клиента Telegram
client.disconnect()