from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_statistics_keyboard() -> InlineKeyboardMarkup:
    """Клавіатура екрану статистики — тільки «Назад в меню»"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Назад в меню",
                callback_data="back_to_main"
            )
        ]
    ])
    return keyboard
