from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.agents.strategy_agent import generate_strategy

router = APIRouter()


@router.get("/recommendations")
def strategy_recommendations():

    db: Session = SessionLocal()

    result = generate_strategy(db)

    db.close()

    return result