from aiogram import Bot, F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from classes.state_classes import Admin
from config import config
from db import db, tests_query
from keyboards import keyboards


router = Router()

ADMIN_ID = int(config.admin_id.get_secret_value())
DEV_ID = int(config.developer_id.get_secret_value())

FORBIDDEN_IDS = {
    'admin_id': 0,
    'developer_id': 0
}


@router.message(
    F.text == '❌ Отмена',
    (F.from_user.id == ADMIN_ID) | (F.from_user.id == DEV_ID),
    StateFilter(Admin)
)
@router.message(
    Command('admin'),
    (F.from_user.id == ADMIN_ID) | (F.from_user.id == DEV_ID)
)
async def admin_start(message: Message, state: FSMContext):
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
async def admin_massage_mail(message: Message, state: FSMContext, bot: Bot):
    users = await db.get_all_users()
    for user in users:
        user_id = user['telegram_id']
        if user_id not in FORBIDDEN_IDS.values():
            try:
                await message.send_copy(chat_id=user_id)
            except Exception:
                pass
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
    tests = await tests_query.get_all_tests()

    for test in tests:
        message += f'{test["test_id"]} - {test["test_name"]}\n'

    await callback.message.answer(
        message
    )

@router.callback_query(Admin.choosing_command, F.data == 'admin_users')
async def check_users(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    users_data = await db.get_all_users()
    message = f'В базе данных {len(users_data)} объекта.\n'
    for user in users_data:
        message += f'@{user['username']} - {user['first_name']}\n'

    await callback.message.answer(
        text=message
    )