from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext

from db.tests import get_test_by_data, get_question_by_test, get_tests
from keyboards.keyboards import dynamic_keyboard_builder, inline_keyboard_builder
from classes.state_classes import Test


router = Router()


@router.callback_query(StateFilter(None), F.data.in_([test.test_name for test in get_tests()]))
async def start_test(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Test.test_in_progress)
    test = get_test_by_data(callback.data)
    question = get_question_by_test(test.id)
    question_text, right_answer = question.text, question.right_answer
    await state.update_data(
        test_id=test.id,
        right_answer=right_answer
        #TODO: add number of buttons from test.number_of_answers
    )
    await callback.answer()
    await callback.message.answer(
        text=question_text,
        #TODO: add number of buttons from test.number_of_answers
        reply_markup=dynamic_keyboard_builder(2).as_markup(resize_keyboard=True)
    )


@router.message(StateFilter(Test.test_in_progress), F.text.isdigit())
async def proceed_answer(message: Message, state: FSMContext):
    user_data = await state.get_data()
    right_answer = user_data.get("right_answer")
    test_id = user_data.get("test_id")
    await message.answer("Правильно!") if message.text == right_answer else await message.answer(f"Неправильно... Правильный ответ - {right_answer}")
    question = get_question_by_test(test_id)
    question_text, right_answer = question.text, question.right_answer
    await state.update_data(
        right_answer=right_answer
    )
    await message.answer(
        text=question_text,
        #TODO: add number of buttons from test.number_of_answers
        reply_markup=dynamic_keyboard_builder(2).as_markup(resize_keyboard=True)
    )


@router.message(StateFilter(Test.test_in_progress), Command('stop'))
async def cancel_test(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        'Возврат к выбору теста...',
        reply_markup=inline_keyboard_builder(get_tests()).as_markup(resize_keyboard=True)
    )