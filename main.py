from fastapi import FastAPI
from database import engine, Base
from models import buyer, invoice, item

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def health():
    return {"status":"ok"}