from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_payment_keyboard() -> InlineKeyboardMarkup:
    """Клавіатура екрану оплати"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Я оплатив",
                callback_data="i_paid"
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


def get_confirmation_keyboard() -> InlineKeyboardMarkup:
    """Клавіатура екрану підтвердження — тільки «Назад в меню»"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Назад в меню",
                callback_data="back_to_main"
            )
        ]
    ])
    return keyboard
