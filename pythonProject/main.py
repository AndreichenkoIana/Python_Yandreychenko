import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import config

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

API_TOKEN = config.token

# Создаем экземпляр класса бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.")


@dp.message(Command("help"))
async def send_help(message: types.Message):
    await message.answer("Кажется, Вам нужна помощь. К сожалению, я сейчас ничем помочь не могу. Меня еще этому не научили.")


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


# Запускаем бота
if __name__ == '__main__':
    asyncio.run(main())
