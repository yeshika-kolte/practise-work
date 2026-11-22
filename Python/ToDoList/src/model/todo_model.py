from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped,mapped_column

from src.db.config_db import Base

class Todo(Base):
    __tablename__ ="todos"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    title:Mapped[str]=mapped_column(String(100),nullable=False)
    priority:Mapped[int]=mapped_column(String(10),nullable=False)
    description:Mapped[str]=mapped_column(String(500),nullable=False)
