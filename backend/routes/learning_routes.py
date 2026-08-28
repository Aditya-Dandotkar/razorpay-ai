from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.agents.learning_agent import generate_learning_insights

router = APIRouter()


@router.get("/insights")
def learning_insights():

    db: Session = SessionLocal()

    result = generate_learning_insights(db)

    db.close()

    return result