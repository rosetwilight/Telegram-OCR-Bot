import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from PIL import Image
import pytesseract

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Приветик 😘\nПришли мне изображение с текстом, а я тебе верну всё в буквочках 🧚‍♀️")

@dp.message(F.photo)
async def handle_photo(message: Message, bot: Bot):
    await message.answer("Обрабатываю фото... 📸 Подожди чуть-чуть, мой хороший 💋")

    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    downloaded = await bot.download_file(file.file_path)

    image_path = "temp_image.jpg"
    with open(image_path, "wb") as f:
        f.write(downloaded.getvalue())

    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang="eng+rus").strip()
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
