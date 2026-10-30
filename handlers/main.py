
import asyncio

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import ADMIN_ID
from keyboards.main import get_start_keyboard

main_router = Router()


# ==================== КАДРИ АНІМАЦІЇ ====================

BOOT_FRAMES = [
    """
<pre>
┌──────────────────────────────────┐
│          BTC SCANNER             │
│            SYSTEM v1.0           │
└──────────────────────────────────┘

root@btc-scanner:~# ./initialize

[....] INITIALIZING SYSTEM...
</pre>
""",

    """
<pre>
┌──────────────────────────────────┐
│          BTC SCANNER             │
│            SYSTEM v1.0           │
└──────────────────────────────────┘

root@btc-scanner:~# ./initialize

[ OK ] CORE INITIALIZED
[....] LOADING MODULES...
</pre>
""",

    """
<pre>
┌──────────────────────────────────┐
│          BTC SCANNER             │
│            SYSTEM v1.0           │
└──────────────────────────────────┘

root@btc-scanner:~# ./initialize

[ OK ] CORE INITIALIZED
[ OK ] MODULES LOADED
[....] CHECKING INTERFACE...
</pre>
""",

    """
<pre>
┌──────────────────────────────────┐
│          BTC SCANNER             │
│            SYSTEM v1.0           │
└──────────────────────────────────┘

[ OK ] CORE INITIALIZED
[ OK ] MODULES LOADED
[ OK ] INTERFACE READY

SYSTEM STATUS: ONLINE

&gt;&gt;&gt; no gods, no masters,
         only math &lt;&lt;&lt;

root@btc-scanner:~# _
</pre>
"""
]
WELCOME_TEXT = BOOT_FRAMES[-1]

# ==================== ГОЛОВНЕ МЕНЮ ====================

@main_router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    """Анімація запуску термінала"""

    # Сповіщення адміну про новий /start
    if ADMIN_ID and ADMIN_ID != 0:
        try:
            name = message.from_user.full_name or "Невідомий"
            username = f"@{message.from_user.username}" if message.from_user.username else f"#{message.from_user.id}"
            await message.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"👤 Користувач натиснув /start\n\nІм'я: {name}\nID: <code>{message.from_user.id}</code>\nUsername: {username}",
                parse_mode="HTML"
            )
        except Exception:
            pass

    # Відправляємо перший кадр
    sent_message = await message.answer(
        BOOT_FRAMES[0],
        parse_mode="HTML"
    )

    # Послідовно відтворюємо наступні кадри
    for frame in BOOT_FRAMES[1:]:
        await asyncio.sleep(0.8)

        await sent_message.edit_text(
            frame,
            parse_mode="HTML"
        )

    # Додаємо кнопки після завершення анімації
    await sent_message.edit_reply_markup(
        reply_markup=get_start_keyboard()
    )
