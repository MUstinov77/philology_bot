from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine(
    "sqlite:///db.sqlite3"
)

def create_session():
    with Session(engine) as session:
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise

def session_provider(session: Session = create_session()):
    return session

def init_db():
    Base