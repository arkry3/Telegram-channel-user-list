# Список участников телеграм канала/группы
This script allows you to get the list of all participants of a Telegram channel/group via a bot, both as messages and an Excel table. (Only if you have admin rights in the channel/group, otherwise the code will not work).

## Setup Before Running the Code
### 1. Install the following libraries before using:
- telethon
- pandas
- openpyxl
- python-dotenv
---
Note: If you encounter an issue with entering your account password in the terminal on the first run, the problem might be the following:

The main issue lies in the library file /telethon/client/auth.py on line 23 - the getpass.getpass() method doesn't work in the PyCharm console where the bot is running, causing the program to freeze.

A possible solution is to modify line 23 as follows:

`password: typing.Union[typing.Callable[[], str], str] = lambda: getpass.getpass('Please enter your password: '),`

на

`password: typing.Union[typing.Callable[[], str], str] = lambda: input('Please enter your password: '),`

---
### 2. Create a Bot and Authenticate with Telegram Applications
You can easily find guides on how to do this on YouTube.
You also need to create a group with the bot where the list will be sent.
### 3. Создайте файл `.env`
In the project folder, create a `confidential.env` file and enter the following:

`API_ID=YOURAPIID`

`API_HASH=YOURAPIHASH`

`BOT_TOKEN=YOURBOTTOKEN`

`GROUP_LINK=YOURGROUPLINKWITHBOT`

`CHANNEL_LINK=YOURCHANNELORGROUPLINK`

`TABLE_PATH=YOURTABLEPATH`
## Running the Code
Now simply create two files: `empty_table.py` and `tg_user_list.py` in the folder with the table.

That’s it, you’re ready to use the code!
