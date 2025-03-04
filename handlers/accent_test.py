import sqlite3


from aiogram.types import Message
from keyboards import keyboards
from aiogram import Router, F
from aiogram.filters import StateFilter, Command

from aiogram.fsm.context import FSMContext
from classes.state_classes import Test


router = Router()


con = sqlite3.connect('db.sqlite')
cur = con.cursor()


@router.message(StateFilter(None), Command('accent_test'))
@router.message(StateFilter(None), F.text.lower() == 'правильное ударение')
async def start_test(message: Message, state: FSMContext):
    await state.set_state(Test.test_in_progress)
    query = cur.execute('''
        SELECT question, right_answer
        FROM questions
        LEFT JOIN test_type
        ON questions.test_type_id = 1
        ORDER BY RANDOM()
        LIMIT 1
    ''')
    question, right_answer = query.fetchone()
    await state.update_data(
        question=question,
        right_answer=right_answer
    )
    await message.answer(
        question,
        reply_markup=keyboards.KEYBOARD_ANSWERS
    )

@router.message(Test.test_in_progress, F.text.isdigit())
async def proceed_answer(message: Message, state: FSMContext):
    user_data = await state.get_data()
    right_answer = user_data.get('right_answer')
    if message.text == right_answer:
        await message.answer(
            'Верно!',
            reply_markup=keyboards.KEYBOARD_ANSWERS
        )
    else:
        await message.answer(
            f'Неверно. Правильным должен быть {right_answer}',
            reply_markup=keyboards.KEYBOARD_ANSWERS
        )
    query = cur.execute('''
        SELECT question, right_answer
        FROM questions
        LEFT JOIN test_type
        ON questions.test_type_id = 1
        ORDER BY RANDOM()
        LIMIT 1
    ''')
    question, right_answer = query.fetchone()
    await state.update_data(question=question, right_answer=right_answer)
    await message.answer(question, reply_markup=keyboards.KEYBOARD_ANSWERS)



@router.message(Test.test_in_progress, F.text.lower() == 'стоп')
async def cancel_test(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Возврат к выбору теста...',
                         reply_markup=keyboards.KEYBOARD_CHOOSING_TEST)
