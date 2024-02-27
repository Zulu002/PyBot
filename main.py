from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
with open('telegram_bot_key.txt', 'r') as file:
    bot_key = file.readline().strip()


async  def get_start(message: Message, bot:Bot):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}. Рад тебя видеть")
    await message.reply(f"Привет {message.from_user.first_name}. Рад тебя видеть")
    await message.answer(f"Привет {message.from_user.first_name}. Рад тебя видеть")

async def start():
    bot = Bot(token=bot_key)
    dp = Dispatcher()
    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())