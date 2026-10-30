from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_start_keyboard() -> InlineKeyboardMarkup:
    """Головна клавіатура"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔑 ОТРИМАТИ ДОСТУП",
                callback_data="get_access"
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙️ Як це працює",
                callback_data="how_it_works"
            )
        ],
        [
            InlineKeyboardButton(
                text="📊 СТАТИСТИКА",
                callback_data="statistics"
            )
        ]
    ])
    return keyboard
