from sqlalchemy.orm import Session

from backend.models.customer import Customer
from backend.models.transaction import Transaction


def generate_strategy(db: Session):

    customers = db.query(Customer).all()

    strategies = []

    for customer in customers:

        transactions = (
            db.query(Transaction)
            .filter(Transaction.customer_id == customer.id)
            .all()
        )

        total_amount = sum(t.amount for t in transactions)

        if total_amount > 100000:
            risk = "HIGH"
            strategy = "Immediate recovery escalation and executive review"

        elif total_amount > 50000:
            risk = "MEDIUM"
            strategy = "Schedule follow-up call and offer payment plan"

        else:
            risk = "LOW"
            strategy = "Continue regular engagement"

        strategies.append(
            {
                "customer_id": customer.id,
                "customer_name": customer.customer_name,
                "risk_level": risk,
                "recommended_strategy": strategy
            }
        )

    return strategies