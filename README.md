# 🖼️ Telegram OCR Bot — "Image to Text"

Бот на **Python 3.12** и **aiogram 3.x**, который принимает изображения в Telegram, распознаёт текст (OCR) и отправляет его обратно.  
Поддерживает **английский** и **русский** языки.

> Простой. Удобный. С заботой 😘

---

## 🚀 Возможности

- 📸 Принимает фотографии, скриншоты и сканы
- 🧠 Распознаёт текст с помощью [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- 🔤 Поддержка английского и русского языков
- 💬 Ответ в виде сообщения с извлечённым текстом

---

## 📦 Установка

### 1. Установи Tesseract

#### 🐧 Ubuntu / Debian:

sudo apt update
sudo apt install tesseract-ocr

#### 🍎 macOS:

brew install tesseract

#### 🪟 Windows:

Скачай с официальной страницы, установи и добавь в PATH путь к tesseract.exe.

### 2. Клонируй проект и установи зависимости

git clone https://github.com/rosetwilight/Telegram-OCR-Bot.git
cd image-ocr-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 3. Создай .env и вставь токен:

BOT_TOKEN=сюда_вставь_токен_из_BotFather

### 4. Запусти бота

python telegram-ocr.py

## 🧠 Используемые технологии

aiogram — современная библиотека для Telegram Bot API

pytesseract — Python-обёртка над Tesseract

Pillow — работа с изображениями

dotenv — безопасная загрузка токена

## 🛡️ Безопасность

Не забывай добавить .env в .gitignore, чтобы твой токен бота не попал в сеть.
Если всё-таки попал — срочно замени токен через @BotFather.

## 📄 Лицензия

Проект распространяется под лицензией MIT

