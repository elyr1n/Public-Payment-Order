import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.start import router as start
from app.core.callbacks import router as callbacks
from app.core.states import router as states


async def main():
    load_dotenv()

    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()

    dp.include_router(start)
    dp.include_router(callbacks)
    dp.include_router(states)

    logging.basicConfig(filename="info.log", level=logging.INFO)

    print("Бот запущен!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
