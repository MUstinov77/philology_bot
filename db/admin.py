from sqlalchemy import select
from sqlalchemy.orm import Session

from .db import engine
from .models import User, Test


def get_users():
    with Session(engine) as session:
        query = select(User)
        result = session.execute(query)
        return result.all()

# async def get_tests():
#     session: Session = session_provider()
#     query = select(Test)
#     result = session.execute(query)
#     return result.all()
