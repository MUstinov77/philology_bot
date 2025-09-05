from sqlalchemy import select
from sqlalchemy.orm import Session

from .db import engine
from .models import User


def get_user(telegram_id: int = None):
    with Session(engine) as session:
        query = select(User).where(User.telegram_id == telegram_id)
        result = session.execute(query)
        return result.first()


def add_user(user_data):
    with Session(engine) as session:

        user = User(**user_data)
        try:
            session.add(user)
            session.commit()
        except Exception as e:
            print(e)
            return False
    return True
