from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)

    telegram_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column()
    first_name: Mapped[str] = mapped_column()

    status: Mapped[str] = mapped_column(default='common')

    last_result: Mapped[str] = mapped_column()

class Test(Base):
    __tablename__ = "tests"

    id: Mapped[str] = mapped_column(primary_key=True, unique=True)
    test_name: Mapped[str] = mapped_column(unique=True)
    questions = relationship("Question", back_populates="test")

class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    text: Mapped[str] = mapped_column()
    right_answer: Mapped[str] = mapped_column()

    test_id: Mapped[int] = mapped_column(ForeignKey("tests.id"))
    test = relationship("Test", back_populates="questions")
