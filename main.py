from openai import AsyncOpenAI
import asyncio
import os
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url="https://api.proxyapi.ru/openai/v1")
router = Router()
messages = []


def reset_messages():
    """
    Функция очистки истории сообщений контекста
    """
    messages.clear()


def update(message, role, content):
    """
    Функция обновления списка сообщений
    """
    message.append({"role": role, "content": content})


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    """
    Функция очистки контекста и начала сообщений по команде /start
    """
    reset_messages()
    await message.reply("Здравствуйте, чем я могу Вам помочь?")
    await state.clear()


async def gpt3(message: types.Message):
    """
    Добавление контекста
    """
    update(messages, 'user', message.text)
    response = await client.chat.completions.create(
        messages=[{"role": "user",
                   "content": str(message)}],
        model="gpt-3.5-turbo"
    )
    print(messages)
    print(response)
    return response


@router.message(F.text)
async def generate(message: Message, state: FSMContext):
    """
        Отправка сообщения, ожидание ответа
    """
    response = await gpt3(message)
    await message.reply(response.choices[0].message.content)


async def main():
    """
        Инициализация бота
    """
    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN_TG"))
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    """
        Точка входа
    """
    asyncio.run(main())
