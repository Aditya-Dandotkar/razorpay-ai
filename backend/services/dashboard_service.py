from sqlalchemy.orm import Session

from backend.agents.revenue_agent import (
    generate_revenue_summary,
    revenue_leakage_summary
)

from backend.agents.learning_agent import (
    generate_learning_insights
)


def get_dashboard_overview(db: Session):

    revenue_summary = generate_revenue_summary(db)

    leakage_summary = revenue_leakage_summary(db)

    learning_summary = generate_learning_insights(db)

    return {
        "total_customers":
            revenue_summary["total_customers"],

        "total_revenue":
            revenue_summary["total_revenue"],

        "high_risk_customers":
            revenue_summary["high_risk_customers"],

        "medium_risk_customers":
            revenue_summary["medium_risk_customers"],

        "low_risk_customers":
            revenue_summary["low_risk_customers"],

        "total_revenue_leakage":
            leakage_summary["total_revenue_leakage"],

        "top_recommendation":
            leakage_summary["recommendation"],

        "insights":
            learning_summary["insights"],
        "total_revenue":
            revenue_summary["total_revenue"],
    }

def get_risk_summary(db: Session):

    revenue_summary = generate_revenue_summary(db)

    return {
        "high_risk_customers":
            revenue_summary["high_risk_customers"],

        "medium_risk_customers":
            revenue_summary["medium_risk_customers"],

        "low_risk_customers":
            revenue_summary["low_risk_customers"]
    }

def get_leakage_summary(db: Session):

    leakage = revenue_leakage_summary(db)

    return leakage


def get_agent_insights(db: Session):

    insights = generate_learning_insights(db)

    return insights