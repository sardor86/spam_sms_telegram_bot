from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from state import WritePhoneNumber
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['cansel'], state='*')
async def start_or_help_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply('Отменена')


@dp.message_handler(commands=['start', 'help'])
async def start_or_help_command(message: types.Message):
    await message.reply('Чтобы начать спамить напишите /begin')


@dp.message_handler(commands=['begin'])
async def start_or_help_command(message: types.Message):
    await message.reply('Напишите нам номер например 998991234567')
    await WritePhoneNumber.number.set()


if __name__ == '__main__':
    executor.start_polling(dp)
