import os
from dotenv import load_dotenv

# Завантаження змінних з .env файлу
load_dotenv()

# Telegram Bot Token (від @BotFather)
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Адміністратор бота (Telegram user ID)
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# Wallet address for USDT payments (TRC20)
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS", "")
