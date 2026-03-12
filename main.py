import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.photo, F.caption.contains('#расписание'))
async def pin_schedule(message: Message):
    try:
        await bot.pin_chat_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception:
        pass

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
