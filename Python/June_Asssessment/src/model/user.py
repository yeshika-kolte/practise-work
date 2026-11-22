from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.config.db import Base

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    posts:Mapped[list["Post"]] = relationship("Post",back_populates="user", cascade="all, delete-orphan")