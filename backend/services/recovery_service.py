from sqlalchemy.orm import Session

from backend.models.customer import Customer
from backend.models.transaction import Transaction


def get_recovery_recommendations(db: Session):

    customers = db.query(Customer).all()

    recommendations = []

    for customer in customers:

        transactions = (
            db.query(Transaction)
            .filter(Transaction.customer_id == customer.id)
            .all()
        )

        total_amount = sum(t.amount for t in transactions)

        if total_amount > 100000:
            risk = "HIGH"
            action = "Escalate Recovery Team"

        elif total_amount > 50000:
            risk = "MEDIUM"
            action = "Email + Follow-up Call"

        else:
            risk = "LOW"
            action = "Friendly Reminder"

        recommendations.append(
            {
                "customer_id": customer.id,
                "customer_name": customer.customer_name,
                "risk_level": risk,
                "recommended_action": action
            }
        )

    return recommendations