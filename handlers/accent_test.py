from aiogram.types import Message
from keyboards import keyboards
from aiogram import Router, F
from aiogram.filters import StateFilter, Command

from aiogram.fsm.context import FSMContext

from db import db
from classes.state_classes import Test


router = Router()




@router.message(StateFilter(None), Command('accent_test'))
async def start_test(message: Message, state: FSMContext):
    await state.set_state(Test.test_in_progress)
    telegram_id = message.from_user.id
    user_data = await db.get_user(telegram_id)
    if not user_data:
        await db.add_user(
            telegram_id=telegram_id,
            username=message.from_user.username,
            first_name=message.from_user.first_name
        )
    question, right_answer = await db.get_question(test_type_id=1)
    await state.update_data(
        question=question,
        right_answer=right_answer
    )
    await message.answer(
        'Выберите вариант в котором правильно поставлено ударение\n'
        'Вызовите команду /stop, если хотите прервать тест'
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
    question, right_answer = await db.get_question(test_type_id=1)
    await state.update_data(question=question, right_answer=right_answer)
    await message.answer(question, reply_markup=keyboards.KEYBOARD_ANSWERS)


@router.message(Test.test_in_progress, Command('stop'))
async def cancel_test(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Возврат к выбору теста...',
                         reply_markup=keyboards.KEYBOARD_CHOOSING_TEST)
