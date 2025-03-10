from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.formatting import Text, Bold
from keyboards import keyboards
from db import db

router = Router()




@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    if state:
        await state.clear()
    telegram_id = message.from_user.id
    user_data = await db.get_user(telegram_id)
    if not user_data:
        await db.add_user(
            telegram_id=telegram_id,
            username=message.from_user.username,
            first_name=message.from_user.first_name
        )
    content = Text(
        'Hello, ',
        Bold(message.from_user.full_name),
        '! Choose an action...'
    )
    keyboard = keyboards.KEYBOARD_START
    await message.answer(**content.as_kwargs(),
                         reply_markup=keyboard)


@router.message(F.text.lower() == 'помощь')
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Этот бот умеет проводить тестирование на '
                         'знание правил русского языка.\n'
                         'Чтобы начать тестирование, выберите команду <b>Начать тест</b> внизу экрана'
                         ' или введите её самостоятельно.\n'
                         'Если Вы правильно ответите, то бот выведет соответсвующую команду.\n'
                         'В противном случае он выведет верный ответ.\n\n'
                         ''
                         'Также в меню в левом нижнем углу экрана\n'
                         'есть список всех команд для упраления ботом'
                         )
