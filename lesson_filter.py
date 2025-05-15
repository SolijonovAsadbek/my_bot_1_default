import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(F.photo)
async def photo_handler(msg: Message):
    await msg.send_copy(chat_id=msg.chat.id)
    await msg.reply('Siz rasm yubordingiz!')


@dp.message(F.document)
async def photo_handler(msg: Message):
    await msg.send_copy(chat_id=msg.chat.id)
    await msg.reply('Siz doc yubordingiz!')


@dp.message(F.location)
async def loc_handler(msg: Message):
    await msg.send_copy(chat_id=msg.chat.id)
    lat = msg.location.latitude
    lon = msg.location.longitude
    await msg.reply(f'Siz loc yubordingiz!\n'
                    f'lat: {lat}\n'
                    f'lon: {lon}')


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
