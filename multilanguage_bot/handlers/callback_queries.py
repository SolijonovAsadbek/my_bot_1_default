from aiogram.types import CallbackQuery
from aiogram import F, Router

from multilanguage_bot.utils.db.postgres_db import pg

call_router = Router()


@call_router.callback_query(F.data.in_({'uz', 'ru', 'en'}))  # Eng katta filter
async def uz_callback_handler(call: CallbackQuery):
    if call.data == 'uz':
        await call.message.answer(text=f"🇺🇿 O'zbek tilni tanladingiz!")
    elif call.data == 'ru':
        await call.message.answer(text=f"🇷🇺 Вы выбрали русский!")
    elif call.data == 'en':
        await call.message.answer(text=f"🇺🇸 You choose English language")
    pg.update_lang(chat_id=call.message.chat.id, lang=call.data)
