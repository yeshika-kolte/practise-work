from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped ,mapped_column
from src.db.db_config import Base

class Department(Base):
    __tablename__ = 'department'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    department_name:Mapped[str] = mapped_column(String(100),unique=True)
    HOD : Mapped[str] = mapped_column(String(100))
