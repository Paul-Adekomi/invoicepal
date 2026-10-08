from fastapi import APIRouter, HTTPException
from schemas import InvoiceCreate
from database import SessionLocal
from models.invoice import Invoice
from models.item import Item
router = APIRouter()

@router.post("/invoices")
def create_invoice(invoice: InvoiceCreate):
    db = SessionLocal()
    try:
        new_invoice = Invoice(buyer_id=invoice.buyer_id, invoice_number=invoice.invoice_number, currency=invoice.currency, due_date=invoice.due_date)

        db.add(new_invoice)
        db.flush()

        for entry in invoice.items:
            new_item = Item(invoice_id=new_invoice.id, description=entry.description, quantity=entry.quantity, unit_price=entry.unit_price)
            db.add(new_item)
        db.commit()    

        return {"id":new_invoice.id, "invoice_number":new_invoice.invoice_number}
    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=400, detail="Could not create invoice")
    finally:
        db.close()

