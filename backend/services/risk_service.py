from sqlalchemy.orm import Session

from backend.models.customer import Customer
from backend.models.transaction import Transaction


def calculate_customer_risk(db: Session):

    customers = db.query(Customer).all()

    print("Customers found:", len(customers))

    results = []

    for customer in customers:

        print("Processing customer:", customer.customer_name)

        transactions = (
            db.query(Transaction)
            .filter(Transaction.customer_id == customer.id)
            .all()
        )

        print("Transactions:", transactions)

        total_amount = sum(t.amount for t in transactions)

        if total_amount > 100000:
            risk = "HIGH"
        elif total_amount > 50000:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        results.append({
            "customer_id": customer.id,
            "customer_name": customer.customer_name,
            "total_transaction_amount": total_amount,
            "risk_level": risk
        })

    return results