import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from app.handlers import router
from dotenv import load_dotenv


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN_TG"))
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
