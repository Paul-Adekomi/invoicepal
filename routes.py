from fastapi import APIRouter
from schemas import InvoiceCreate

router = APIRouter()

@router.post("/invoices")
def create_invoice(invoice: InvoiceCreate):
    return invoice
