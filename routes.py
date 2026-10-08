from fastapi import APIRouter
from schemas import InvoiceCreate
from database import SessionLocal
from models import Invoice, Item

router = APIRouter()

@router.post("/invoices")
def create_invoice(invoice: InvoiceCreate):
    return invoice
