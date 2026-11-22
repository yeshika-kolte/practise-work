from sqlalchemy import Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column
from src.db.db_config import Base
class Order(Base):
    __tablename__ = "orders"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    order_number:Mapped[str]=mapped_column(String(100),nullable=False)
    status:Mapped[str]=mapped_column(String(100),nullable=False)
    subtotal:Mapped[float]=mapped_column(Numeric(10,2) ,nullable=False)
    shipping_cot:Mapped[float]=mapped_column(Numeric(10,2) ,nullable=False)
    tax: Mapped[float]=mapped_column(Numeric(10,2) ,nullable=False)
    total_amount:Mapped[float]=mapped_column(Numeric(10,2),nullable=False)
    user_id:Mapped[int]=mapped_column(Integer,ForeignKey('user.id'))
    address_id:Mapped[int]=mapped_column(Integer,ForeignKey('address.id'))





