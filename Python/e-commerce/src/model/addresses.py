from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base

class Address(Base):
    __tablename__ = "address"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    full_name:Mapped[str]=mapped_column(String(100),nullable=False)
    phone:Mapped[String]=mapped_column(String(100),nullable=False)
    address:Mapped[String]=mapped_column(String(100),nullable=False)
    city:Mapped[String]=mapped_column(String(100),nullable=False)
    state:Mapped[String]=mapped_column(String(100),nullable=False)
    postal_code:Mapped[String]=mapped_column(String(100),nullable=False)
    country:Mapped[String]=mapped_column(String(100),nullable=False)
    user_id:Mapped[int]=mapped_column(Integer,ForeignKey('user.id'))

