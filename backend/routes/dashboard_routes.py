from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal

from backend.services.dashboard_service import (
    get_dashboard_overview,
    get_risk_summary,
    get_leakage_summary,
    get_agent_insights
)

router = APIRouter()


@router.get("/overview")
def dashboard_overview():

    db: Session = SessionLocal()

    result = get_dashboard_overview(db)

    db.close()

    return result


@router.get("/risk-summary")
def risk_summary():

    db: Session = SessionLocal()

    result = get_risk_summary(db)

    db.close()

    return result


@router.get("/leakage-summary")
def leakage_summary():

    db: Session = SessionLocal()

    result = get_leakage_summary(db)

    db.close()

    return result


@router.get("/agent-insights")
def agent_insights():

    db: Session = SessionLocal()

    result = get_agent_insights(db)

    db.close()

    return result