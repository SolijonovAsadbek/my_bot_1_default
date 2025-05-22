from aiogram import html, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from multilanguage_bot.keyboards.inline import three_languages
from multilanguage_bot.utils.helper.translater import google_translate

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!\n\n"
    #                      f"Tilni tanlang: ",
    #                      reply_markup=three_languages())
    datas = google_translate(message.chat.id)
    await message.answer(datas['start'])


@start_router.message(Command('help'))
async def help_me(message: Message):
    datas = google_translate(message.chat.id)
    await message.answer(datas['help'])


@start_router.message(Command('set_lang'))
async def set_lang(message: Message):
    datas = google_translate(message.chat.id)
    await message.answer(datas['set_lang'], reply_markup=three_languages())
