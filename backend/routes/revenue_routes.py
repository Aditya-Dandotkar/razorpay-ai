from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.agents.revenue_agent import generate_revenue_summary

router = APIRouter()


@router.get("/summary")
def revenue_summary():

    db: Session = SessionLocal()

    result = generate_revenue_summary(db)

    db.close()

    return result