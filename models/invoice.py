from database import Base
from sqlalchemy import Column, Integer, String

class Invoice(Base):
    __tablename__ = "invoice"
    id = Column(Integer, primary_key=True, autoincrement=True)