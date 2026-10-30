from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.payment import get_payment_keyboard, get_confirmation_keyboard
from config import WALLET_ADDRESS, ADMIN_ID

payment_router = Router()


PAYMENT_TEXT = f"""
💎 <b>ОТРИМАТИ ДОСТУП</b>

📦 <b>Продукт</b>
<code>scanner.exe</code> — повна версія програми

💰 <b>Вартість:</b> 20 USDT

🔗 <b>Мережа:</b> TRC20 (Tron)

👛 <b>Адреса для оплати:</b>
<code>{WALLET_ADDRESS}</code>

📋 <b>Як отримати доступ:</b>

1. Надішліть 20 USDT на вказану адресу.
2. Натисніть кнопку «Я оплатив».
3. Дочекайтеся підтвердження платежу.

⏳ Доступ надається після перевірки оплати.

⚠️ Переконайтеся, що обрали мережу TRC20.
"""


@payment_router.callback_query(F.data == "get_access")
async def cb_get_access(callback: CallbackQuery) -> None:
    """Екран оплати за доступ."""

    await callback.message.edit_text(
        PAYMENT_TEXT,
        parse_mode="HTML",
        reply_markup=get_payment_keyboard()
    )

    await callback.answer()


@payment_router.callback_query(F.data == "i_paid")
async def cb_i_paid(callback: CallbackQuery) -> None:
    """Користувач натиснув «Я оплатив» — сповістити адміна."""

    user = callback.from_user
    username = user.username or "Немає"
    user_id = user.id
    first_name = user.first_name or "—"

    admin_message = (
        f"🔔 <b>НОВЕ ПІДТВЕРДЖЕННЯ ОПЛАТИ</b>\n\n"
        f"👤 <b>Користувач:</b> {first_name}\n"
        f"🆔 <b>ID:</b> <code>{user_id}</code>\n"
        f"📛 <b>Username:</b> <code>@{username}</code>\n\n"
        f"⚠️ Перевірте оплату та надайте доступ."
    )

    # Відправка повідомлення адміну
    if ADMIN_ID and ADMIN_ID != 0:
        try:
            await callback.bot.send_message(
                chat_id=ADMIN_ID,
                text=admin_message,
                parse_mode="HTML"
            )
        except Exception:
            pass

    await callback.message.edit_text(
        """✅ <b>ДЯКУЄМО!</b>

Ваше підтвердження отримано.

Ми перевіримо оплату та надамо доступ найближчим часом.

⏳ Зазвичай це займає кілька хвилин.

🔙 Натисніть кнопку нижче, щоб повернутися в меню.""",
        parse_mode="HTML",
        reply_markup=get_confirmation_keyboard()
    )

    await callback.answer("✅ Підтвердження відправлено!")