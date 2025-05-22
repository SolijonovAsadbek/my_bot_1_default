from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram import F, Router

from multilanguage_bot.utils.db.postgres_db import pg
from multilanguage_bot.utils.helper.translater import google_translate

call_router = Router()


@call_router.callback_query(F.data.in_({'uz', 'ru', 'en'}))  # Eng katta filter
async def uz_callback_handler(call: CallbackQuery):
    pg.update_lang(chat_id=call.message.chat.id, lang=call.data)
    datas = google_translate(call.message.chat.id)
    await call.message.answer(datas['choose_lang'], reply_markup=ReplyKeyboardRemove())
