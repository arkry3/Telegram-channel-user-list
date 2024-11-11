from telethon import TelegramClient, events, utils
import pandas as pd
from empty_table import empty_table
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='confidential.env')

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
chat_link = os.getenv('CHAT_LINK')
file_path = os.getenv('FILE_PATH')
channel_link = os.getenv('CHANNEL_LINK')


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
user_data = {'Name': []}


@bot.on(events.NewMessage(pattern=r'\.users', chats=chat_link))
async def handler(event):
    users = await bot.get_participants(channel_link)
    for user in users:
        if user.username is not None:
            user_data['Name'].append(user.username)
            await bot.send_message(entity=chat_link, message=user.username)
        else:
            await bot.send_message(entity=chat_link, message='ОШИБКА')
            user_data['Name'].append('ОШИБКА, НЕТУ НИКА')
    empty_table(file_path)
    df = pd.DataFrame(user_data)
    df.to_excel(file_path, index=False, engine='openpyxl')
    await bot.send_message(
        entity=chat_link, message='Тот же список в виде Excel таблицы'
    )
    await bot.send_file(entity=chat_link, file=file_path)


bot.start()
bot.run_until_disconnected()
