function InsightsPanel({ insights }) {
    return (
        <div
            style={{
                background: "#0f172a",
                color: "white",
                padding: "20px",
                borderRadius: "12px",
                marginTop: "20px"
            }}
        >
            <h2>Agent Insights</h2>

            {insights?.map((item, index) => (
                <p key={index}>• {item}</p>
            ))}
        </div>
    )
}

export default InsightsPanel