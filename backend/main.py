from fastapi import FastAPI

from backend.database import engine, Base

import backend.models.customer
import backend.models.transaction
import backend.models.recovery

from backend.routes.customer_routes import router as customer_router
from backend.routes.transaction_routes import router as transaction_router
from backend.routes.recovery_routes import router as recovery_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    customer_router,
    prefix="/customers",
    tags=["Customers"]
)

app.include_router(
    transaction_router,
    prefix="/transactions",
    tags=["Transactions"]
)

app.include_router(
    recovery_router,
    prefix="/recoveries",
    tags=["Recoveries"]
)

@app.get("/")
def home():
    return {"message": "Revenue Guardian API Running"}