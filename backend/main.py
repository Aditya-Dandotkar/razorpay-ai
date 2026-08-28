from fastapi import FastAPI

from backend.database import engine, Base

import backend.models.customer
import backend.models.transaction
import backend.models.recovery

from backend.routes.customer_routes import router as customer_router
from backend.routes.transaction_routes import router as transaction_router
from backend.routes.recovery_routes import router as recovery_router
from backend.routes.risk_routes import router as risk_router
from backend.routes.churn_routes import router as churn_router
from backend.routes.rootcause_routes import router as rootcause_router
from backend.routes.revenue_routes import router as revenue_router
from backend.routes.strategy_routes import router as strategy_router
from backend.routes.revenue_leakage_routes import router as revenue_leakage_router
from backend.routes.agent_routes import router as agent_router

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

app.include_router(
    risk_router,
    prefix="/risks",
    tags=["Risks"]
)

app.include_router(
    churn_router,
    prefix="/churn",
    tags=["Churn"]
)

app.include_router(
    rootcause_router,
    prefix="/rootcause",
    tags=["Root Cause"]
)

app.include_router(
    revenue_router,
    prefix="/revenue",
    tags=["Revenue Agent"]
)

app.include_router(
    strategy_router,
    prefix="/strategy",
    tags=["Strategy Agent"]
)

app.include_router(
    revenue_leakage_router,
    prefix="/revenue-leakage",
    tags=["Revenue Leakage"]
)

app.include_router(
    agent_router,
    prefix="/agents",
    tags=["Agents"]
)



@app.get("/")
def home():
    return {"message": "Revenue Guardian API Running"}