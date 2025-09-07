from sqlalchemy import select

from .db import session_provider
from .models import User, Test


def get_tests():
    session = session_provider()
    query = select(Test)
    result = session.execute(query)
    return result.scalars().all()

def get_users():
    session = session_provider()
    query = select(User)
    result = session.execute(query)
    return result.scalars().all()
