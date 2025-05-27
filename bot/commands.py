import asyncio
import logging
import random
import sys
from datetime import datetime, timedelta
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand, BotCommandScopeAllPrivateChats
# from aiogram.utils.chat_member import ADMINS
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
ADMINS = getenv('ADMINS').split(',')


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")


async def set_bot_commands(bot: Bot):
    private_commands = [
        BotCommand(command='start', description='Botni ishga tushurish'),
        BotCommand(command='help', description='Yordam olish botdan'),
        BotCommand(command='play', description='Guess Number o`yinini o`ynash'),
        BotCommand(command='register', description='Ro`yxatdan o`tish'),
        BotCommand(command='set', description='Nimadur o`zgartirish')
    ]

    await bot.set_my_commands(
        commands=private_commands,
        scope=BotCommandScopeAllPrivateChats()
    )


@dp.startup()
async def notify_admins_on_startup(bot: Bot):
    for admin in ADMINS:
        await bot.send_message(admin, text='Bot ishga tushdi!')


@dp.shutdown()
async def notify_admins_on_shutdown(bot: Bot):
    for admin in ADMINS:
        await bot.send_message(admin, text='Bot o`chdi!')


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # dp.startup.register(notify_admins_on_startup)
    # dp.shutdown.register(notify_admins_on_shutdown)

    await set_bot_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
