from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

KEY_TEST = types.KeyboardButton(text='Начать тест')
KEY_HELP = types.KeyboardButton(text='Помощь')
KEY_STOP = types.KeyboardButton(text='Отмена')
KEY_ACCENT_TEST = types.KeyboardButton(text='Правильное ударение')

KEY_ANSWER_1 = types.KeyboardButton(text='1')
KEY_ANSWER_2 = types.KeyboardButton(text='2')
KEY_ANSWER_3 = types.KeyboardButton(text='3')
KEY_ANSWER_4 = types.KeyboardButton(text='4')

# inline buttons
KEY_ADMIN_MAIL = types.InlineKeyboardButton(
    text='📩Рассылка', callback_data='admin_mail'
)
KEY_ADMIN_BACK = types.InlineKeyboardButton(
    text='🔙Выйти', callback_data='admin_back'
)
KEY_ADMIN_TEST = types.InlineKeyboardButton(
    text='📝Тесты', callback_data='admin_tests'
)
KEY_ADMIN_USERS = types.InlineKeyboardButton(
    text='👥Пользователи', callback_data='admin_users'
)
KEY_CANCEL = types.KeyboardButton(
    text='❌ Отмена'
)

KEYBOARD_START = ReplyKeyboardBuilder(
    [
        [KEY_TEST, KEY_HELP]
    ]
)

KEYBOARD_CHOOSING_TEST = ReplyKeyboardBuilder(
    [
        [KEY_ACCENT_TEST,]
    ]
)
KEYBOARD_ANSWERS = ReplyKeyboardBuilder(
    [
        [KEY_ANSWER_1, KEY_ANSWER_2],
    ]
)

ADMIN_CHOOSE_KEYBOARD = InlineKeyboardBuilder(
    [
        [
            KEY_ADMIN_MAIL, KEY_ADMIN_USERS
        ],
        [
            KEY_ADMIN_TEST, KEY_ADMIN_BACK
        ]
    ]
)
KEYBOARD_CANCEL = ReplyKeyboardBuilder(
    [
        [KEY_CANCEL]
    ]
)

KEYBOARD_START = KEYBOARD_START.as_markup(resize_keyboard=True)
KEYBOARD_CHOOSING_TEST = KEYBOARD_CHOOSING_TEST.as_markup(resize_keyboard=True)
KEYBOARD_ANSWERS = KEYBOARD_ANSWERS.as_markup(resize_keyboard=True)
