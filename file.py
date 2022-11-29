import os
import dotenv

# Команда dotenv.find_dotenv() находит файл .env    Вместо нее можно написать dotenv.load_dotenv('.env')
dotenv.load_dotenv(dotenv.find_dotenv())
# Находим ключ для переменной bot. Альтенативная запись bot = os.getenv('bot_token')
# os.environ это переменные среды
BOT_TOKEN = os.environ['BOT_TOKEN']


print(BOT_TOKEN)



