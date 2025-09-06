from sqlalchemy import select
from sqlalchemy.orm import Session

from .db import engine, session_provider
from .models import User, Test


def get_users():
    session = session_provider()
    query = select(User)
    result = session.execute(query)
    return result.all()

# async def get_tests():
#     session: Session = session_provider()
#     query = select(Test)
#     result = session.execute(query)
#     return result.all()
