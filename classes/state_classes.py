from aiogram.fsm.state import StatesGroup, State


class Test(StatesGroup):
    test_in_progress = State()
