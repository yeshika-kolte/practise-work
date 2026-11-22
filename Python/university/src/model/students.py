from sqlalchemy import String ,Integer,Date
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base
class Students(Base):
    __tablename__ = 'students'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    student_name:Mapped[str] = mapped_column(String(100),nullable=False)
    gender:Mapped[str] = mapped_column(String(100),nullable=False)
    dob:Mapped[str] = mapped_column(String(100),nullable=False)
    email:Mapped[str] = mapped_column(String(100),nullable=False,unique=True)
    phone:Mapped[str] = mapped_column(String(100),nullable=False)
    address:Mapped[str] = mapped_column(String(100),nullable=False)
    admission:Mapped[Date] = mapped_column(Date,nullable=False)
