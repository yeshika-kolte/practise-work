from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DB_URL = 'mysql+pymysql://root:yeshika%401611@localhost:3306/university'

engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(bind=engine,autoflush=False,autocommit=False)

class Base(DeclarativeBase):
    pass