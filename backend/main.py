from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models import Base

from routers.product import router as product_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ayurvedic Inventory Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)


@app.get("/")
def root():
    return {
        "message": "Backend Running Successfully"
    }