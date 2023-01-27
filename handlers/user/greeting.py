from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import dp
from states import UserGreeting


@dp.message(Command(commands=["start", "run"]))
async def start_command(message: Message, state: FSMContext):
    await message.answer(f"Привет, {message.from_user.full_name}\n"
                         f"Укажите, сколько Вам лет?")
    await state.set_state(UserGreeting.enter_age)


@dp.message(
    UserGreeting.enter_age,
    F.func(lambda message: message.text.isnumeric())
)
async def keep_user_age(message: Message, state: FSMContext):
    await state.update_data(user_age=int(message.text))
    
    await message.answer("Отлично! Теперь введите основной язык для разработки")
    await state.set_state(UserGreeting.enter_programming_language)


@dp.message(UserGreeting.enter_programming_language, F.text)
async def keep_user_programming_language(message: Message, state: FSMContext):
    state_data = await state.get_data()
    
    await message.answer(
        "<b>Вот и познакомились  =)</b>\n\n"
        f"Возраст — {state_data.get('user_age')}\n"
        f"Язык программирования — {message.text}"
    )
