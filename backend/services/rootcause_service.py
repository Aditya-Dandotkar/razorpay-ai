from sqlalchemy.orm import Session

from backend.models.customer import Customer
from backend.models.transaction import Transaction


def analyze_root_cause(db: Session):

    customers = db.query(Customer).all()

    results = []

    for customer in customers:

        transactions = (
            db.query(Transaction)
            .filter(Transaction.customer_id == customer.id)
            .all()
        )

        total_amount = sum(t.amount for t in transactions)

        # Risk Logic

        if total_amount > 100000:
            risk = "HIGH"

        elif total_amount > 50000:
            risk = "MEDIUM"

        else:
            risk = "LOW"

        # Root Cause Logic

        if risk == "LOW":
            cause = "Healthy transaction activity"

        elif risk == "MEDIUM":
            cause = "Declining transaction volume"

        else:
            cause = "High financial exposure"

        results.append(
            {
                "customer_id": customer.id,
                "customer_name": customer.customer_name,
                "risk_level": risk,
                "root_cause": cause
            }
        )

    return results