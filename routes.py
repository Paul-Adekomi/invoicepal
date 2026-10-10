from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from schemas import InvoiceCreate
from database import SessionLocal
from models.invoice import Invoice
from models.item import Item
import uuid
router = APIRouter()

@router.post("/invoices")
def create_invoice(invoice: InvoiceCreate):
    db = SessionLocal()
    temp_num = str(uuid.uuid4())
    try:
        new_invoice = Invoice(buyer_id=invoice.buyer_id, invoice_number=temp_num, currency=invoice.currency, due_date=invoice.due_date)

        db.add(new_invoice)
        db.flush()

        new_invoice.invoice_number = f"INV-{new_invoice.id:04d}"

        for entry in invoice.items:
            new_item = Item(invoice_id=new_invoice.id, description=entry.description, quantity=entry.quantity, unit_price=entry.unit_price)
            db.add(new_item)
        db.commit()    

        return {"id":new_invoice.id, "invoice_number":new_invoice.invoice_number}
    except IntegrityError as e:   
        print(e)
        db.rollback()
        message = str(e.orig)

        if "invoice_number" in message:
            raise HTTPException(status_code=409, detail="Invoice number already exists!")
        elif "buyer_id" in message:
            raise HTTPException(status_code=409, detail="Buyer does not exist")   
        else:     
            raise HTTPException(status_code=409, detail="Invoice conflicts with existing data")
    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=400, detail="Could not create invoice")
    finally:
        db.close()

