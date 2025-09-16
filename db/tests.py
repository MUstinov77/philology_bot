from sqlalchemy import select
from sqlalchemy.sql.expression import func

from db.db import session_provider
from db.models import Question, Test

def get_question_by_test(test_id: int):
    session = session_provider()
    query = select(Question).where(Question.test_id == test_id).order_by(func.random()).limit(1)
    result = session.execute(query)
    return result.scalar_one_or_none()

def get_tests():
    session = session_provider()
    query = select(Test)
    result = session.execute(query)
    return result.scalars().all()

def get_test_by_data(callback_data):
    session = session_provider()
    query = select(Test).where(Test.test_name == callback_data)
    result = session.execute(query)
    return result.scalar_one_or_none()