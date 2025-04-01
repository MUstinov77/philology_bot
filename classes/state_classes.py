from aiogram.fsm.state import State, StatesGroup


class Test(StatesGroup):
    test_in_progress = State()


class Admin(StatesGroup):
    choosing_command = State()
    admin_mail = State()
    tests_command = State()
