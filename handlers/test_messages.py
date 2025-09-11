from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import Message

from db.tests import get_tests
from keyboards import keyboards

router = Router()


@router.message(StateFilter(None), F.text.lower() == 'начать тест')
async def chose_test(message: Message):
    # TODO: add fetching tests from db and refactor keybord for callbacks
    tests = get_tests()
    tests_message = "Выберите тест: \n"
    for test in tests:
        tests_message += f"{test.id}. /{test.test_name}\n"
    await message.answer(
        tests_message,
        reply_markup=keyboards.dynamic_keyboard_builder(len(tests)).as_markup(resize_keyboard=True)
    )


@router.message(StateFilter(None), F.text.lower() == 'отмена')
async def proceed_answer(message: Message):
    await message.answer(
        'Вы прервали выбор теста',
        reply_markup=keyboards.KEYBOARD_START
    )
