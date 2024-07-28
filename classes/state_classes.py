from aiogram.fsm.state import StatesGroup, State


class Test(StatesGroup):
    right_answer = ''
    test_in_progress = State()


class Statistics:
    all_questions = 0
    right_answers_count = 0
    questions_and_answers_list: list[tuple] = []


