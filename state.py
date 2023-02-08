from aiogram.dispatcher.filters.state import StatesGroup, State


class WritePhoneNumber(StatesGroup):
    number = State()
