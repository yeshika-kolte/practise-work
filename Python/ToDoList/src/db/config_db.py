from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DB_URL ="mysql+aiomysql://root:yeshika%401611@localhost:3306/todo"

engine = create_async_engine(DB_URL,echo=True)
sessionLocal = async_sessionmaker(engine ,expire_on_commit=False)

class Base(DeclarativeBase):
    pass