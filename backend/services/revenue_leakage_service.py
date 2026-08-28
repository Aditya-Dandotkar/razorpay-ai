from sqlalchemy.orm import Session

from backend.models.customer import Customer
from backend.models.transaction import Transaction
from backend.models.recovery import Recovery


def calculate_revenue_leakage(db: Session):

    customers = db.query(Customer).all()

    results = []

    for customer in customers:

        transactions = (
            db.query(Transaction)
            .filter(Transaction.customer_id == customer.id)
            .all()
        )

        recoveries = (
            db.query(Recovery)
            .filter(Recovery.customer_id == customer.id)
            .all()
        )

        total_transaction_amount = sum(
            t.amount for t in transactions
        )

        total_recovered_amount = sum(
            r.recovery_amount for r in recoveries
        )

        leakage = (
            total_transaction_amount -
            total_recovered_amount
        )

        results.append(
            {
                "customer_id": customer.id,
                "customer_name": customer.customer_name,
                "transaction_amount": total_transaction_amount,
                "recovered_amount": total_recovered_amount,
                "revenue_leakage": leakage
            }
        )

    return results