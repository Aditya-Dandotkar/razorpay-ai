from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.services.rootcause_service import analyze_root_cause

router = APIRouter()


@router.get("/analysis")
def rootcause_analysis():

    db: Session = SessionLocal()

    result = analyze_root_cause(db)

    db.close()

    return result