from aiogram import html
from aiogram.filters import CommandStart
from aiogram.types import Message

from multilanguage_bot.keyboards.inline import three_languages
from multilanguage_bot.app import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!\n\n"
                         f"Tilni tanlang: ",
                         reply_markup=three_languages())
