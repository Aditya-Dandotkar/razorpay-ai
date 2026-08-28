export async function getDashboardOverview() {
    const response = await fetch(
        "http://127.0.0.1:8000/dashboard/overview"
    );

    return await response.json();
}

export async function getRiskSummary() {
    const response = await fetch(
        "http://127.0.0.1:8000/dashboard/risk-summary"
    );

    return await response.json();
}

export async function getAgentInsights() {
    const response = await fetch(
        "http://127.0.0.1:8000/dashboard/agent-insights"
    );

    return await response.json();
}