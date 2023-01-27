from aiogram.fsm.state import StatesGroup, State


class UserGreeting(StatesGroup):
    """ Запрос информации у пользователя при запуске Бота """
    
    enter_age = State()
    enter_programming_language = State()
