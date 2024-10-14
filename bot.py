# Импорт основных библиотек aiogram
from aiogram import Dispatcher, Bot, types
# Импорт телеграм токена
from config import TELEGRAM_BOT_TOKEN

# Создание объекта бота и dispatcher'а для работы с ботом
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды старт
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f"{message.from_user.full_name} я на хуке!")

# Эхо
@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f"{message.text}")