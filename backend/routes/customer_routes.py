from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models.customer import Customer

router = APIRouter()

@router.get("/")
def get_customers():
    db: Session = SessionLocal()

    customers = db.query(Customer).all()

    result = []

    for customer in customers:
        result.append({
            "id": customer.id,
            "customer_name": customer.customer_name,
            "email": customer.email,
            "gst_number": customer.gst_number
        })

    db.close()

    return result