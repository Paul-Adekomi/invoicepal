from database import Base
from sqlalchemy import Column, Integer, String


class Buyer(Base):
    __tablename__ = "buyer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
