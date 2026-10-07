from database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Numeric


class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey("invoice.id"), nullable=False)
    description = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(12, 2), nullable=False)
