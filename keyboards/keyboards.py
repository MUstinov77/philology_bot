from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types


KEY_TEST = types.KeyboardButton(text='Начать тест')
KEY_HELP = types.KeyboardButton(text='Помощь')
KEY_STOP = types.KeyboardButton(text='Отмена')
KEY_RETRY = types.KeyboardButton(text='/retry')
KEY_ACCENT_TEST = types.KeyboardButton(text='Правильное ударение')
KEY_SHORT_TEST = types.KeyboardButton(text='/short_test')

KEY_ANSWER_1 = types.KeyboardButton(text='1')
KEY_ANSWER_2 = types.KeyboardButton(text='2')
KEY_ANSWER_3 = types.KeyboardButton(text='3')
KEY_ANSWER_4 = types.KeyboardButton(text='4')

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

KEYBOARD_START = KEYBOARD_START.as_markup(resize_keyboard=True)
KEYBOARD_CHOOSING_TEST = KEYBOARD_CHOOSING_TEST.as_markup(resize_keyboard=True)
KEYBOARD_ANSWERS = KEYBOARD_ANSWERS.as_markup(resize_keyboard=True)
