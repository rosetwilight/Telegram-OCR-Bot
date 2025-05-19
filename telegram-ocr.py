import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os
import pytesseract
from PIL import Image

# Указываем явно путь к Tesseract и папке с языками
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/5/tessdata"


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Запоминаем выбранный язык распознавания
user_langs = {}

def language_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang-ru"),
            InlineKeyboardButton(text="🇬🇧 Английский", callback_data="lang-en"),
            InlineKeyboardButton(text="🌐 Рус + Англ", callback_data="lang-ru+en"),
        ]
    ])

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Приветик! 😘\nВыбери язык текста на картинках, которые будешь присылать мне:",
        reply_markup=language_menu()
    )

@dp.callback_query(F.data.startswith("lang-"))
async def set_lang(callback: types.CallbackQuery):
    lang_map = {
        "ru": "rus",
        "en": "eng",
        "ru+en": "rus+eng"
    }
    lang_key = callback.data.split("-")[1]
    lang = lang_map.get(lang_key, "eng")
    user_langs[callback.from_user.id] = lang
    readable = {
        "rus": "Русский",
        "eng": "Английский",
        "rus+eng": "Русский + Английский"
    }.get(lang, lang)
    await callback.answer()
    await callback.message.answer(f"Отлично! Буду искать текст на: {readable} 🧠\nТеперь просто пришли мне изображение!")


@dp.message(F.photo)
async def handle_photo(message: Message, bot: Bot):
    lang = user_langs.get(message.from_user.id)
    if not lang:
        await message.answer("Пожалуйста, сначала выбери язык текста через /start 💬")
        return

    await message.answer("Обрабатываю фото... 📸")

    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    downloaded = await bot.download_file(file.file_path)

    image_path = "temp_image.jpg"
    with open(image_path, "wb") as f:
        f.write(downloaded.getvalue())

    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang=lang).strip()
        if not text:
            text = "Ой, я не смогла ничего распознать 😔"
    except Exception as e:
        text = f"Что-то пошло не так… {e}"

    await message.answer(f"📝 Вот, что я вижу:\n\n{text}")
    os.remove(image_path)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
