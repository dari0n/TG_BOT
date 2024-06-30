import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

bot = Bot(token='7254120142:AAEjOGe09hwxhCCSv3tq6KAaBSkHB6puaoo')
dispatcher = Dispatcher()


@dispatcher.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello world')


async def main():
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
