from aiogram.types import Message
from keyboards import keyboards
from aiogram import Router, F
from aiogram.filters import StateFilter, Command

from aiogram.fsm.context import FSMContext
from random import randint
from classes.state_classes import Test


router = Router()


accent_test = Test()


@router.message(StateFilter(None), Command('accent_test'))
@router.message(StateFilter(None), F.text.lower() == 'неправильное ударение')
async def start_test(message: Message, state: FSMContext):

    await state.set_state(accent_test.test_in_progress)
    await message.answer('Придумываю тест...\n'
                         'Выберите вариант, в котором правильно поставлено ударение\n'
                         'Учитывайте контекст, в круглых скобках\n'
                         'Напишите <b>Отмена</b>, чтобы вернуться к выбору теста')
    await message.answer(
                         reply_markup=keyboards.KEYBOARD_ANSWERS)


@router.message(accent_test.test_in_progress, F.text.isdigit())
async def process_answer(message: Message):
    if message.text == accent_test.right_answer:
        await message.answer('Правильно!')
    else:
        await message.answer('Неправильно...\n'
                             f'Правильный ответ - {accent_test.right_answer}'
                             )
    question, accent_test.right_answer = WRONG_ACCENT_QUESTIONS[randint(1, len(WRONG_ACCENT_QUESTIONS))]
    await message.answer(question)


@router.message(accent_test.test_in_progress, F.text.lower() == 'отмена')
async def cancel_test(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Возврат к выбору теста...',
                         reply_markup=keyboards.KEYBOARD_CHOOSING_TEST)
