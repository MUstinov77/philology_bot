from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import Message

from keyboards import keyboards

router = Router()


@router.message(StateFilter(None), F.text.lower() == 'начать тест')
async def chose_test(message: Message):
    # TODO: add fetching tests from db and refactor keybord for callbacks
    await message.answer('Выберите тест:\n'
                         '/accent_test - тест на постановку ударения в словах',
                         reply_markup=keyboards.KEYBOARD_CHOOSING_TEST)


@router.message(StateFilter(None), F.text.lower() == 'отмена')
async def proceed_answer(message: Message):
    await message.answer('Вы прервали выбор теста',
                         reply_markup=keyboards.KEYBOARD_START)
