from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.services.revenue_leakage_service import calculate_revenue_leakage

router = APIRouter()


@router.get("/analysis")
def revenue_leakage_analysis():

    db: Session = SessionLocal()

    result = calculate_revenue_leakage(db)

    db.close()

    return result