from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models.transaction import Transaction

router = APIRouter()

@router.get("/transactions/")
def get_transactions():
    db: Session = SessionLocal()

    transactions = db.query(Transaction).all()

    result = []

    for transaction in transactions:
        result.append({
            "id": transaction.id,
            "customer_id": transaction.customer_id,
            "amount": transaction.amount,
            "transaction_type": transaction.transaction_type
        })

    db.close()

    return result