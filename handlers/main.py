
import asyncio

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

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
