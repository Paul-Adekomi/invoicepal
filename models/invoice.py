from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
class Invoice(Base):
    __tablename__ = "invoice"
    id = Column(Integer, primary_key=True, autoincrement=True)
    buyer_id = Column(Integer, ForeignKey("buyer.id"), nullable=False)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())