from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DB_URl = "mysql+aiomysql://root:yeshika%401611@localhost:3306/todop"

create_engine = create_async_engine(DB_URl, echo=True)
SessionLocal = async_sessionmaker(create_engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_session():
    async with SessionLocal.begin() as session:
        yield session

