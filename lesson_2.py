import asyncio
import logging
import random
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(Command('start'))  # HTML format bilan ishlash.
async def command_start_handler(message: Message, mylist: [int]) -> None:
    text = (f"b yoki strong: <b>Aiogram</b>\n"
            f"i yoki em: <i>Aiogram</i>\n"
            f"u yoki ins <u>Aiogram</u>\n"
            f"s, strike yoki del: <del>Aiogram</del>\n"
            f"span yoki tg-spoiler: <span class='tg-spoiler'>Aiogram</span>\n"
            # f"Link: <a href=\"https://core.telegram.org/bots/api\">tg api html format</a>\n"
            f"CR7 rasm: <a href=\"https://m.media-amazon.com/images/I/81eSkgnULzL.jpg\">CR7</a>\n"
            f"Python Code <code>print('Hello world!')</code>\n"
            f"<pre><code class=\"language-python\"> pre-formatted fixed-width code block written in the Python programming language</code></pre>\n")
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!\n\n" + text)


@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.reply('/start - botni ishga tushurish\n'
                        '/help - yordam')


@dp.message()  # Any message
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
