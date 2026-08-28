from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.services.churn_service import predict_customer_churn

router = APIRouter()


@router.get("/churn-analysis")
def churn_analysis():

    db: Session = SessionLocal()

    result = predict_customer_churn(db)

    db.close()

    return result