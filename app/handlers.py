from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command

router = Router()


@router.message(Command('start'))
async def start(message: Message):
    await message.reply("Test TG")
