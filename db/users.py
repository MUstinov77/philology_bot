from sqlalchemy import select
from sqlalchemy.orm import Session

from .db import session_provider
from .models import User


async def get_user(session: Session = session_provider(), telegram_id: int = None):
    query = select(User).where(User.telegram_id == telegram_id)
    result = session.execute(query)
    return result.first()


async def add_user(user_data, session: Session = session_provider()):
    user = User(**user_data)
    try:
        session.add(user)
    except Exception as e:
        print(e)
        return False
    return True
