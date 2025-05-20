from aiogram.types import CallbackQuery
from aiogram import F, Router

call_router = Router()


@call_router.callback_query(F.data.in_({'uz', 'ru', 'en'}))  # Eng katta filter
async def uz_callback_handler(call: CallbackQuery):
    if call.data == 'uz':
        await call.message.answer(text=f"🇺🇿 O'zbek tilni tanladingiz!")
    elif call.data == 'ru':
        await call.message.answer(text=f"🇷🇺 Вы выбрали русский!")
    elif call.data == 'en':
        await call.message.answer(text=f"🇺🇸 You choose English language")
