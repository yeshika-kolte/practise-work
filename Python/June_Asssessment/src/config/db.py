from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime,func


DB_URL =('mysql+aiomysql://root:yeshika%401611@localhost:3306/juneblogs')


engine = create_async_engine(DB_URL)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
