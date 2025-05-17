import asyncio
import logging
import random
import sys
from datetime import datetime, timedelta
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums.dice_emoji import DiceEmoji
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp['started_at'] = datetime.now()  # dict
dp['my_birthday'] = datetime(year=1999, month=11, day=1)  # time


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")


@dp.message(Command('dice'))
async def send_dicemoji(message: Message, bot: Bot):
    emojies = [DiceEmoji.BASKETBALL, DiceEmoji.BOWLING, DiceEmoji.DICE, DiceEmoji.FOOTBALL]
    emoji = emojies[random.randint(0, 3)]
    await bot.send_dice(chat_id=message.chat.id, emoji=DiceEmoji.DICE)
    await message.answer_dice(emoji=DiceEmoji.BOWLING)


@dp.message(Command('work_time'))
async def worked_time(message: Message, started_at: datetime, my_birthday: datetime):
    worked_at = datetime.now() - started_at
    await message.reply(f'Bot {worked_at.seconds} sekundan beri ishlab turibdi!\n\n'
                        f'Birthday: {my_birthday}')


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
