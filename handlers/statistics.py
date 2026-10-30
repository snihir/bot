import asyncio
import random

from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.statistics import get_statistics_keyboard

statistics_router = Router()

users = 53
satoshi = 1_237_846_291


def stats_text():
    return f"""
<pre>
┌────────────────────────────────┐
│       SYSTEM STATISTICS        │
└────────────────────────────────┘

[ USERS ]
TOTAL USERS       : {users:,}

[ SATOSHI ]
TOTAL SATOSHI     : {satoshi:,}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AUTO UPDATE: EVERY 1 MINUTE
</pre>
"""


@statistics_router.callback_query(F.data == "statistics")
async def show_statistics(callback: CallbackQuery):
    global users, satoshi

    if callback.message is None:
        await callback.answer()
        return

    await callback.message.edit_text(
        stats_text(),
        parse_mode="HTML",
        reply_markup=get_statistics_keyboard()
    )

    await callback.answer()

    async def update():
        global users, satoshi

        minutes = 0

        while True:
            await asyncio.sleep(60)

            satoshi += random.randint(1_000, 50_000)
            minutes += 1

            if minutes >= 30:
                users += random.randint(1, 2)
                minutes = 0

            await callback.message.edit_text(
                stats_text(),
                parse_mode="HTML",
                reply_markup=get_statistics_keyboard()
            )

    asyncio.create_task(update())