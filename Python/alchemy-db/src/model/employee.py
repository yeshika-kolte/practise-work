from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from src.db.dbConfig import Base

class Employee(Base):
    __tablename__ =  'emp'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(100), nullable=False)
    salary:Mapped[float] = mapped_column(Numeric(10,2), nullable=False)

    def __repr__(self):
        return f"{self.id} : {self.name} : {self.salary}"