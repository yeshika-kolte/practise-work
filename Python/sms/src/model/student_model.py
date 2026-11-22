from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db_config import Base


class Student(Base):
    __tablename__ = "students"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    email:Mapped[str] = mapped_column(String(100),nullable=False,unique=True)
    course:Mapped[str] = mapped_column(String(100),nullable=False)
    age:Mapped[int] = mapped_column(Integer,nullable=False)