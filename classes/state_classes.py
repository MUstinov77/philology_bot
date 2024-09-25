from aiogram.fsm.state import StatesGroup, State


class Test(StatesGroup):
    test_type_id: int = None
    question = ''
    right_answer = ''
    test_in_progress = State()


class Statistics:
    all_questions = 0
    right_answers_count = 0
    #questions_and_answers_list: list[tuple] = []

    def count_right_percent(self):
        return round(self.right_answers_count / self.all_questions * 100, 1)

    def clear_stats(self):
        self.all_questions = 0
        self.right_answers_count = 0

