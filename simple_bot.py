"""
Простой Telegram бот для тестирования подключения.
"""
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import config

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start."""
    await update.message.reply_text(
        f'Привет! Бот работает!\n'
        f'Ваш Chat ID: {update.effective_chat.id}'
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /help."""
    await update.message.reply_text('Используйте /start для начала работы.')


def main() -> None:
    """Запуск бота."""
    try:
        # config.py сам проверит наличие токена и выбросит ошибку если его нет
        token = config.TELEGRAM_BOT_TOKEN
    except ValueError as e:
        print(f"❌ ОШИБКА: {e}")
        print("   Создайте файл .env с переменной TELEGRAM_BOT_TOKEN")
        print("   Получите токен у @BotFather в Telegram")
        return
    
    # Создание приложения
    application = Application.builder().token(token).build()
    
    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Запуск бота
    print("🤖 Запуск Telegram бота...")
    print("   Нажмите Ctrl+C для остановки")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()

