from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from classes.state_classes import Test
from db import tests
from keyboards import keyboards

router = Router()


@router.message(StateFilter(None), F.text.lower() == 'правильное ударение')
@router.message(StateFilter(None), Command('accent_test'))
async def start_test(message: Message, state: FSMContext):
    await state.set_state(Test.test_in_progress)
    question = tests.get_question_by_test(test_id=1)
    text, right_answer = question.text, question.right_answer
    await state.update_data(
        text=text,
        right_answer=right_answer
    )
    await message.answer(
        'Выберите вариант в котором правильно поставлено ударение\n'
        'Вызовите команду /stop, если хотите прервать тест'
    )
    await message.answer(
        text,
        reply_markup=keyboards.KEYBOARD_ANSWERS
    )


@router.message(Test.test_in_progress, F.text.isdigit())
async def proceed_answer(message: Message, state: FSMContext):
    user_data = await state.get_data()
    right_answer = user_data.get('right_answer')
    await message.answer("Right!") if message.text == right_answer else await message.answer(f"wrong! Right answer is {right_answer}")
    question = tests.get_question_by_test(test_id=1)
    text, right_answer = question.text, question.right_answer
    await state.update_data(
        text=text,
        right_answer=right_answer
    )
    await message.answer(text, reply_markup=keyboards.KEYBOARD_ANSWERS)


@router.message(Test.test_in_progress, Command('stop'))
async def cancel_test(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        'Возврат к выбору теста...',
        reply_markup=keyboards.KEYBOARD_CHOOSING_TEST
    )
