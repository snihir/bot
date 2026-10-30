#!/usr/bin/env python3
"""
Bitcoin Scanner Telegram Bot

Бот для надання доступу до Bitcoin Scanner скрипта
з красивим оформленням повідомлень та кнопками.
"""

import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import main_router, payment_router, info_router, navigation_router, statistics_router


# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)


async def on_startup(bot: Bot, dispatcher: Dispatcher) -> None:
    """Логіка при запуску бота"""
    logger.info("🤖 Бот Bitcoin Scanner запущено!")


async def main() -> None:
    """Головна функція запуску бота"""
    # Ініціалізація бота та диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Підключення обробників
    dp.include_router(main_router)
    dp.include_router(payment_router)
    dp.include_router(info_router)
    dp.include_router(navigation_router)
    dp.include_router(statistics_router)
    
    # Реєстрація обробника запуску
    dp.startup.register(on_startup)
    
    # Видалення курсору введення
    await bot.delete_webhook(drop_pending_updates=True)
    
    logger.info("🚀 Бот запущено! Очікування повідомлень...")
    
    # Запуск polling
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logger.info("🛑 Бот зупинено користувачем")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"❌ Помилка запуску бота: {e}")
