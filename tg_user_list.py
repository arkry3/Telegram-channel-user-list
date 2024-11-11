from telethon import TelegramClient, events, utils
import pandas as pd
from empty_table import empty_table
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='confidential.env')

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
group_link = os.getenv('GROUP_LINK')
table_path = os.getenv('TABLE_PATH')
channel_link = os.getenv('CHANNEL_LINK')


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
user_data = {'Name': []}


@bot.on(events.NewMessage(pattern=r'\.users', chats=group_link))
async def handler(event):
    users = await bot.get_participants(channel_link)
    for user in users:
        if user.username is not None:
            user_data['Name'].append(user.username)
            await bot.send_message(entity=group_link, message=user.username)
        else:
            await bot.send_message(entity=group_link, message='ОШИБКА')
            user_data['Name'].append('ОШИБКА, НЕТУ НИКА')
    empty_table(table_path)
    df = pd.DataFrame(user_data)
    df.to_excel(table_path, index=False, engine='openpyxl')
    await bot.send_message(
        entity=group_link, message='Тот же список в виде Excel таблицы'
    )
    await bot.send_file(entity=group_link, file=table_path)


bot.start()
bot.run_until_disconnected()

