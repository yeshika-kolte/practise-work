from sqlalchemy import Integer, String,  Numeric
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base

class Product(Base):
    __tablename__ = 'product'
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    title:Mapped[str]=mapped_column(String(100),nullable=False)
    price:Mapped[float]=mapped_column(Numeric(10,2),nullable=False)
    discount_percent:Mapped[float]=mapped_column(Numeric(10,2),nullable=False)
    brand:Mapped[str]=mapped_column(String(100),nullable=False)
    category:Mapped[str]=mapped_column(String(100),nullable=False)