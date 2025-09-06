from sqlalchemy import select

from .db import session_provider
from .models import User, Test


def get_users(tuples: True | False = None):
    session = session_provider()
    query = select(User)
    result = session.execute(query)
    return result.tuples().all() if tuples else result.all()

def get_tests():
    session = session_provider()
    query = select(Test)
    result = session.execute(query)
    return result.all()
