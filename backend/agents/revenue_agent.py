from sqlalchemy.orm import Session

from backend.models.customer import Customer
from backend.models.transaction import Transaction
from backend.services.revenue_leakage_service import (
    calculate_revenue_leakage
)


def generate_revenue_summary(db: Session):

    customers = db.query(Customer).all()

    high = 0
    medium = 0
    low = 0

    for customer in customers:

        transactions = (
            db.query(Transaction)
            .filter(Transaction.customer_id == customer.id)
            .all()
        )

        total_amount = sum(t.amount for t in transactions)

        if total_amount > 100000:
            high += 1

        elif total_amount > 50000:
            medium += 1

        else:
            low += 1

    summary = (
        f"{high} high risk customers, "
        f"{medium} medium risk customers, "
        f"{low} low risk customers."
    )

    return {
        "total_customers": len(customers),
        "high_risk_customers": high,
        "medium_risk_customers": medium,
        "low_risk_customers": low,
        "summary": summary
    }

    
def revenue_leakage_summary(db: Session):

    leakage_data = calculate_revenue_leakage(db)

    total_leakage = sum(
        item["revenue_leakage"]
        for item in leakage_data
    )

    highest_leakage_customer = max(
        leakage_data,
        key=lambda x: x["revenue_leakage"]
    )

    return {
        "total_revenue_leakage": total_leakage,
        "highest_leakage_customer":
            highest_leakage_customer["customer_name"],
        "highest_leakage_amount":
            highest_leakage_customer["revenue_leakage"],
        "recommendation":
            "Immediate Recovery Campaign"
    }