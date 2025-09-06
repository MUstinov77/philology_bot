from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from classes.state_classes import Admin
from config import config
from db import admin
from keyboards import keyboards
from utils.utils import unpack_sequence

router = Router()

ADMIN_ID = int(config.admin_id.get_secret_value())
DEV_ID = int(config.developer_id.get_secret_value())


@router.message(
    F.text == '❌ Отмена',
    (F.from_user.id == ADMIN_ID) | (F.from_user.id == DEV_ID),
    StateFilter(Admin)
)
@router.message(
    Command('admin'),
    (F.from_user.id == ADMIN_ID) | (F.from_user.id == DEV_ID),
    StateFilter(None)
)
async def admin_start(message: Message, state: FSMContext):
    if state:
        await state.clear()
    await state.set_state(Admin.choosing_command)
    await message.answer(
        '<b>Выберите команду:</b>',
        reply_markup=keyboards.ADMIN_CHOOSE_KEYBOARD.as_markup(
            resize_keyboard=True
        )
    )


@router.callback_query(Admin.choosing_command, F.data == 'admin_mail')
async def handle_massage_for_mail(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Admin.admin_mail)
    await callback.message.answer(
        'Введите сообщение для отправки:',
        reply_markup=keyboards.KEYBOARD_CANCEL.as_markup(
            resize_keyboard=True
        )
    )


@router.message(Admin.admin_mail)
async def admin_massage_mail(message: Message, state: FSMContext):
    users_sequence = admin.get_users()
    for user_id in unpack_sequence(users_sequence, "telegram_id"):
        try:
            await message.send_copy(chat_id=user_id)
        except Exception as e:
            # TODO: add logging
            print(e)
    await state.set_state(Admin.choosing_command)
    await message.answer(
        text='Cообщения отправлены\n'
             '<b>Выберите команду:</b>',
        reply_markup=keyboards.ADMIN_CHOOSE_KEYBOARD.as_markup(
            resize_keyboard=True
        )
    )


@router.callback_query(StateFilter(Admin), F.data == 'admin_back')
async def cancel_command(callback: CallbackQuery,  state: FSMContext):
    await callback.answer()
    await state.clear()
    await callback.message.answer(
        'Вы вышли из панели администратора',
        reply_markup=keyboards.KEYBOARD_START
    )

@router.callback_query(Admin.choosing_command, F.data == 'admin_tests')
async def tests_command(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Admin.tests_command)
    message = f'<b>Тесты</b>:\n'
    test_sequence = admin.get_tests()
    for test_row in test_sequence:
        for test in test_row:
            message += str(test)
    await callback.message.answer(
        message
    )

@router.callback_query(Admin.choosing_command, F.data == 'admin_users')
async def check_users(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    users = admin.get_users(tuples=True)
    message = f'Пользователей в базе: {len(users)}\n'
    for user in users:
        message += str(user[0])

    await callback.message.answer(
        text=message
   )
    await callback.message.answer(
        text='Выберите команду:',
        reply_markup=keyboards.ADMIN_CHOOSE_KEYBOARD.as_markup(
            resize_keyboard=True
        )
    )