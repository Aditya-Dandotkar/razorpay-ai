function RiskCard({ title, value }) {
    return (
        <div
            style={{
                background: "#1e293b",
                color: "white",
                padding: "20px",
                borderRadius: "12px",
                width: "200px",
                textAlign: "center"
            }}
        >
            <h3>{title}</h3>
            <h2>{value}</h2>
        </div>
    )
}

export default RiskCard