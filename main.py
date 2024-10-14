# Импорт основных библиотек fastapi
from fastapi import FastAPI
# Импорт основных библиотек aiogram
from aiogram import types, Dispatcher, Bot
# Импорт бота
from bot import dp, bot
# Импорт телеграм токена и видимой ссылки ngrok
from config import TELEGRAM_BOT_TOKEN, NGROK_TUNNEL_URL

# Создание приложения fastapi
app = FastAPI()
# Создание ссылок для работы с webhook'ом
WEBHOOK_PATH = f"/bot/{TELEGRAM_BOT_TOKEN}"
WEBHOOK_URL = f"{NGROK_TUNNEL_URL}{WEBHOOK_PATH}"

# При старте проверяет корректность вебхука
@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)

# Работа с обновлениями
@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)

# Отключение бота
@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()