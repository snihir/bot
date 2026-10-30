from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.main import get_start_keyboard
from handlers.main import WELCOME_TEXT

navigation_router = Router()


@navigation_router.callback_query(F.data == "back_to_main")
async def cb_back_to_main(callback: CallbackQuery) -> None:
    """Повернення до головного меню"""
    await callback.message.edit_text(
        WELCOME_TEXT,
        parse_mode="HTML",
        reply_markup=get_start_keyboard()
    )
    await callback.answer("🔙 Головне меню")
