from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_back_keyboard() -> InlineKeyboardMarkup:
    """Кнопка назад"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 НАЗАД В МЕНЮ",
                callback_data="back_to_main"
            )
        ]
    ])
    return keyboard


def get_access_keyboard() -> InlineKeyboardMarkup:
    """Клавіатура після доступу"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📥 Завантажити скрипт",
                callback_data="download_script"
            )
        ],
        [
            InlineKeyboardButton(
                text="📖 Інструкція",
                callback_data="instructions"
            ),
            InlineKeyboardButton(
                text="❓ Допомога",
                callback_data="help"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 Назад в меню",
                callback_data="back_to_main"
            )
        ]
    ])
    return keyboard
