from fastapi import FastAPI
from database import engine, Base
from models import buyer, invoice, item
from routes import router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def health():
    return {"status":"ok"}