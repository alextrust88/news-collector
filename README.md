# NewsAgent - Telegram бот для новостей

Простой сервер для работы с Telegram ботом.

## Быстрый старт

### 1. Установите uv (если еще не установлен)
```bash
# Mac/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Или через pip
pip install uv
```

### 2. Установите зависимости
```bash
uv sync
```

### 3. Настройте config.py
Откройте `config.py` и укажите:
- `TELEGRAM_BOT_TOKEN` - получите у @BotFather
- `TELEGRAM_CHAT_ID` - получите у @userinfobot

### 4. Запустите простой бот для проверки
```bash
uv run python simple_bot.py
```

### 5. Проверьте работу
Найдите вашего бота в Telegram и отправьте `/start`

## Подробная инструкция

Смотрите файл `SETUP.md` для пошаговой инструкции по настройке.

