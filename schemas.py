from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Literal
from datetime import date

class ItemCreate(BaseModel):
    description: str
    quantity: int = Field(gt=0)
    unit_price: Decimal

class InvoiceCreate(BaseModel):
    buyer_id: int
    invoice_number: str
    due_date: date | None = None
    items: list[ItemCreate]
    currency: Literal["NGN", "USD"]