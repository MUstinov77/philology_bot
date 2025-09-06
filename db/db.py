from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .base import Base

engine = create_engine(
    "sqlite:///db.sqlite3"
)

def create_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        try:
            session.commit()
        except Exception:
            session.rollback()
            raise

def session_provider() -> Session:
    return next(create_session())

def init_db():
    Base.metadata.create_all(engine)