from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal

from backend.agents.revenue_agent import (
    generate_revenue_summary,
    revenue_leakage_summary
)

router = APIRouter()


@router.get("/revenue-summary")
def get_revenue_summary():

    db: Session = SessionLocal()

    result = generate_revenue_summary(db)

    db.close()

    return result


@router.get("/revenue-leakage-summary")
def get_revenue_leakage_summary():

    db: Session = SessionLocal()

    result = revenue_leakage_summary(db)

    db.close()

    return result