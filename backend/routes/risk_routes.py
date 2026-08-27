from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.services.risk_service import calculate_customer_risk

router = APIRouter()


@router.get("/risk-analysis")
def risk_analysis():

    db: Session = SessionLocal()

    result = calculate_customer_risk(db)

    db.close()

    return result