from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from state import WritePhoneNumber
from config import TOKEN
from spam_sms import begin_spam_sms

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['cansel'], state='*')
async def start_or_help_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply('Отменена')


@dp.message_handler(commands=['start', 'help'])
async def start_or_help_command(message: types.Message):
    await message.reply('Чтобы начать спамить напишите /begin'
                        'Программист из github sardor86')


@dp.message_handler(commands=['begin'])
async def start_spam_sms(message: types.Message):
    await message.reply('Напишите нам номер например 998991234567')
    await WritePhoneNumber.number.set()


@dp.message_handler(lambda message: message.text[:3] == '998' and len(message.text) == 12,
                    state=WritePhoneNumber.number)
async def get_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = int(message.text)

    try:
        phone_number = int(message.text)
    except ValueError:
        await message.reply('Это не номер телефона')
        return None

    async with state.proxy() as data:
        data['phone_number'] = phone_number

    await message.reply('Отправте нам количество итераций')
    await WritePhoneNumber.iteration.set()


@dp.message_handler(lambda message: not message.text[:3] == '998' and not len(message.text) == 12,
                    state=WritePhoneNumber.number)
async def error_get_phone_number(message: types.Message, state: FSMContext):
    await message.reply('Это не номер телефона')


@dp.message_handler(state=WritePhoneNumber.iteration)
async def spam_sms(message: types.Message, state: FSMContext):
    try:
        iteration = int(message.text)
    except ValueError:
        await message.reply('Это не число')
        return None
    async with state.proxy() as data:
        phone_number = data['phone_number']

    begin_spam_sms(phone_number, iteration)
    await message.reply('отправляются сообщения')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp)
