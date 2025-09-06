from sqlalchemy import select
from sqlalchemy.sql.expression import func

from .db import session_provider
from .models import Question

def get_question_by_test(test_id: int):
    session = session_provider()
    query = select(Question).where(Question.test_id == test_id).order_by(func.random()).limit(1)
    result = session.execute(query)
    return result.scalar_one_or_none()