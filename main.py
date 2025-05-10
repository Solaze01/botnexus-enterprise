from aiogram import Bot, Dispatcher
from aiogram.types import Message
from app.config import TOKEN
from app.crm import handle_crm
from app.tasks import handle_task
from app.analytics import handle_analytics

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: Message):
    await message.reply("🤖 Welcome to BotNexus Enterprise!\nUse /crm, /task, or /analytics.")

@dp.message_handler(commands=['crm'])
async def crm_cmd(message: Message):
    await handle_crm(message)

@dp.message_handler(commands=['task'])
async def task_cmd(message: Message):
    await handle_task(message)

@dp.message_handler(commands=['analytics'])
async def analytics_cmd(message: Message):
    await handle_analytics(message)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
