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

    last_result: Mapped[str] = mapped_column(nullable=True)

    # def __repr__(self):
    #     return f"{self.username} {self.first_name} статус-{self.status}\n"

    def __str__(self):
        return  f"{self.username} {self.first_name} статус-{self.status}\n"

class Test(Base):
    __tablename__ = "tests"

    id: Mapped[str] = mapped_column(primary_key=True, unique=True)
    test_name: Mapped[str] = mapped_column(unique=True)
    questions = relationship("Question", back_populates="test")
    # TODO: add test command (/accent_test)
    # test_command: Mapped[str] = mapped_column(unique=True)

    def __str__(self):
        return self.test_name

class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    text: Mapped[str] = mapped_column()
    right_answer: Mapped[str] = mapped_column()

    test_id: Mapped[int] = mapped_column(ForeignKey("tests.id"))
    test = relationship("Test", back_populates="questions")
