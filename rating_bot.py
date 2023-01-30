from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from cfg import *
from counter import get_res
from apscheduler.schedulers.asyncio import AsyncIOScheduler


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def echo_message():
    await bot.send_message('-1001598054361', await get_res(accs.keys()), parse_mode="html")


if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    scheduler.add_job(echo_message, "interval", hours = 6)
    scheduler.start()
    executor.start_polling(dp)
