from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base
class Faculty(Base):
    __tablename__ = 'faculty'
    id:Mapped[int]