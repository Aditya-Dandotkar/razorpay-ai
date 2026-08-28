import { useEffect, useState } from "react";

import SummaryCard from "../components/SummaryCard";
import RiskCard from "../components/RiskCard";
import InsightsPanel from "../components/InsightsPanel";

import {
    getDashboardOverview,
    getRiskSummary,
    getAgentInsights,
} from "../services/api";

function Dashboard() {
    const [overview, setOverview] = useState({});
    const [risk, setRisk] = useState({});
    const [insights, setInsights] = useState([]);

    useEffect(() => {
        loadDashboard();
    }, []);

    async function loadDashboard() {
        const overviewData = await getDashboardOverview();
        const riskData = await getRiskSummary();
        const insightData = await getAgentInsights();

        setOverview(overviewData);
        setRisk(riskData);
        setInsights(insightData.insights || []);
    }

    return (
        <div style={{ padding: "30px" }}>
            <h1>Razorpay AI Dashboard</h1>

            <div
                style={{
                    display: "flex",
                    gap: "20px",
                    marginTop: "20px",
                    flexWrap: "wrap",
                }}
            >
                <SummaryCard
                    title="Customers"
                    value={overview.total_customers}
                />

                <SummaryCard
                    title="Revenue"
                    value={overview.total_revenue}
                />

                <SummaryCard
                    title="Leakage"
                    value={overview.total_revenue_leakage}
                />
            </div>

            <h2 style={{ marginTop: "40px" }}>
                Risk Distribution
            </h2>

            <div
                style={{
                    display: "flex",
                    gap: "20px",
                    marginTop: "20px",
                }}
            >

                <RiskCard
                    title="High Risk"
                    value={risk.high_risk_customers}
                />

                <RiskCard
                    title="Medium Risk"
                    value={risk.medium_risk_customers}
                />

                <RiskCard
                    title="Low Risk"
                    value={risk.low_risk_customers}
                />


            </div>

            <InsightsPanel insights={insights} />
        </div>
    );
}

export default Dashboard;