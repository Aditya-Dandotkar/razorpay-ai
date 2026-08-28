from sqlalchemy.orm import Session

from backend.models.customer import Customer
from backend.models.transaction import Transaction


def predict_customer_churn(db: Session):

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

        # Churn Logic

        if risk == "HIGH":
            churn_probability = 90

        elif risk == "MEDIUM":
            churn_probability = 60

        else:
            churn_probability = 20

        results.append(
            {
                "customer_id": customer.id,
                "customer_name": customer.customer_name,
                "risk_level": risk,
                "churn_probability": churn_probability
            }
        )

    return results