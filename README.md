# Список участников телеграм канала/группы
Позволяет получить список всех участников канала/группы в телеграм с помощью бота в  виде сообщений и таблицы эксель. (Только если у вас есть права админа канала/группы, иначе код работать не будет)

## Настройка перед запуском кода
### 1. Перед использованием необходимо установить слежующие библиотеки:
- telethon
- pandas
- openpyxl
- python-dotenv
---
Примечание: если при первом запуске кода у вас ошибка с вписыванием пароля от аккаунта в терминал, то возможно проблема в следующем:

Основная проблема в файле библиотеки /telethon/client/auth.py в строке 23 - библиотека и метод getpass.getpass() не работает в консоли PyCharm в которой запускается бот, на этом месте   программа и зависает.

Возможное решение проблемы - изменить 23 строку:

`password: typing.Union[typing.Callable[[], str], str] = lambda: getpass.getpass('Please enter your password: '),`

на

`password: typing.Union[typing.Callable[[], str], str] = lambda: input('Please enter your password: '),`

---
### 2. Создание бота и авторизация в приложениях телеграмма
Как это сделать можно легко найти в ютубе. 
Так же вам надо создать группу с ботом в которую будет отправляться список.
### 3. Создайте файл `.env`
В папке с кодом создайте `confidential.env` и впишите в него слудующее:

`API_ID=ВАШАЙДИ`

`API_HASH=ВАШХЭШ`

`BOT_TOKEN=ВАШТОКЕНБОТА`

`GROUP_LINK=ССЫЛКАНАГРУППУСБОТОМ`

`CHANNEL_LINK=ССЫЛКАНАКАНАЛИЛИГРУППУ`

`TABLE_PATH=ПУТЬКТАБЛИЦЕ`
## Запуск кода
Теперь просто создаём два файла `empty_table.py` и `tg_user_list.py` в папке с таблицей. 

На этом всё, теперь вы вожете использовать код. 
