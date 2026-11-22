from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DB_URL="mysql+pymysql://root:yeshika%401611@localhost:3306/alchemy_db"

engine = create_engine(DB_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass

