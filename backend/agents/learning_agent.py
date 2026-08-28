from sqlalchemy.orm import Session

from backend.services.risk_service import calculate_customer_risk
from backend.services.revenue_leakage_service import calculate_revenue_leakage


def generate_learning_insights(db: Session):

    risk_data = calculate_customer_risk(db)

    leakage_data = calculate_revenue_leakage(db)

    high_risk_count = len(
        [c for c in risk_data if c["risk_level"] == "HIGH"]
    )

    medium_risk_count = len(
        [c for c in risk_data if c["risk_level"] == "MEDIUM"]
    )

    total_leakage = sum(
        item["revenue_leakage"]
        for item in leakage_data
    )

    insights = []

    if medium_risk_count > 0:
        insights.append(
            "Medium-risk customers require proactive engagement."
        )

    if high_risk_count > 0:
        insights.append(
            "High-risk customers should be prioritized for recovery actions."
        )

    if total_leakage > 50000:
        insights.append(
            "Revenue leakage is significant and requires immediate attention."
        )

    if not insights:
        insights.append(
            "Customer portfolio appears healthy."
        )

    return {
        "total_revenue_leakage": total_leakage,
        "insights": insights
    }