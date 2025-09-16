from aiogram import F, Router
from aiogram.filters import StateFilter, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from classes.state_classes import Test
from db.tests import get_tests
from keyboards import keyboards

router = Router()


@router.message(StateFilter(None), F.text.lower() == 'начать тест')
async def chose_test(message: Message, state: FSMContext):
    tests = get_tests()
    tests_message = "Выберите тест: \n"
    for test in tests:
        tests_message += f"{test.id}. /{test.test_name}\n"
    await message.answer(
        tests_message,
        reply_markup=keyboards.inline_keyboard_builder(tests).as_markup(resize_keyboard=True)
    )

