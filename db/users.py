from sqlalchemy import select

from .db import session_provider
from .models import User


def get_user(telegram_id: int = None):
    session = session_provider()
    query = select(User).where(User.telegram_id == telegram_id)
    result = session.execute(query)
    return result.one_or_none()

def get_users():
    session = session_provider()
    query = select(User)
    result = session.execute(query)
    return result.scalars().all()


def add_user(user_data):
    session = session_provider()
    user = User(**user_data)
    try:
        session.add(user)
        session.commit()
    except Exception as e:
        # TODO: add logging
        print(e)
        return False
    return True
