from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models.recovery import Recovery
from backend.services.recovery_service import get_recovery_recommendations

router = APIRouter()


@router.get("/")
def get_recoveries():

    db: Session = SessionLocal()

    recoveries = db.query(Recovery).all()

    result = []

    for recovery in recoveries:
        result.append({
            "id": recovery.id,
            "customer_id": recovery.customer_id,
            "recovery_amount": recovery.recovery_amount,
            "status": recovery.status
        })

    db.close()

    return result


@router.get("/recommendations")
def recovery_recommendations():

    db: Session = SessionLocal()

    result = get_recovery_recommendations(db)

    db.close()

    return result