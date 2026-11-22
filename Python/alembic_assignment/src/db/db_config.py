from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DB_URl ='mysql+pymysql://root:yeshika%401611@localhost:3306/product'

engine= create_engine(DB_URl,echo=True)
SessionLocal =sessionmaker(bind=engine,autoflush=False,autocommit=False)

class Base(DeclarativeBase):
    pass