from aiogram import Bot, F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from classes.state_classes import Admin
from config import config
from db import db
from keyboards import keyboards
from utils.messages import func_by_message_type

router = Router()

ADMIN_ID = int(config.admin_id.get_secret_value())
DEV_ID = int(config.developer_id.get_secret_value())

FORBIDDEN_IDS = {
    'admin_id': ADMIN_ID,
    'developer_id': DEV_ID
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
            await func_by_message_type(
                message=message,
                chat_id=user_id,
                bot=bot,
            )
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
