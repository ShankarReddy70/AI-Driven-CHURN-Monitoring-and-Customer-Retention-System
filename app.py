import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from src.predict import predict_new_customer

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Churn AI Dashboard", layout="wide")

# =========================
# PREMIUM CSS
# =========================
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(180deg, #020617, #0f172a);
    color: white;
}
.block-container {
    padding-top: 2rem;
}
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-size: 18px;
}
.metric-card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
# 🚀 Customer Churn Intelligence Platform
### AI-powered retention insights for modern businesses
""")

st.divider()

# =========================
# INPUT SECTION
# =========================
st.subheader("🧾 Customer Profile")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    tenure = st.slider("Tenure (Months)", 0, 72, 12)

with col2:
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

with col3:
    payment = st.selectbox("Payment Method", [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ])
    monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)

total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

# =========================
# INPUT PREP
# =========================
def prepare_input():
    return {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": tenure,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": internet,
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": contract,
        "PaperlessBilling": "Yes",
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

# =========================
# BUTTON
# =========================
if st.button("🔮 Analyze Customer"):

    data = prepare_input()
    pred, prob = predict_new_customer(data)

    st.divider()
    st.subheader("📊 AI Prediction Dashboard")

    colA, colB = st.columns(2)

    # =========================
    # RESULT + KPI
    # =========================
    with colA:
        if pred == 1:
            st.error("⚠️ HIGH CHURN RISK")
        else:
            st.success("✅ LOW CHURN RISK")

        st.metric("Churn Probability", f"{prob:.2f}")

        # KPI CARDS
        c1, c2, c3 = st.columns(3)
        c1.metric("Tenure", tenure)
        c2.metric("Monthly ₹", monthly)
        c3.metric("Contract", contract)

    # =========================
    # GAUGE CHART
    # =========================
    with colB:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prob * 100,
            title={'text': "Risk Score"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#ef4444"},
                'steps': [
                    {'range': [0, 40], 'color': "#22c55e"},
                    {'range': [40, 70], 'color': "#f59e0b"},
                    {'range': [70, 100], 'color': "#ef4444"},
                ]
            }
        ))
        st.plotly_chart(fig, use_container_width=True)

    # =========================
    # DONUT CHART
    # =========================
    st.subheader("📉 Risk Composition")

    fig2 = px.pie(
        values=[prob, 1 - prob],
        names=["Churn Risk", "Retention"],
        hole=0.6,
        color_discrete_sequence=["#ef4444", "#22c55e"]
    )
    st.plotly_chart(fig2, use_container_width=True)

    # =========================
    # PROGRESS BAR
    # =========================
    st.subheader("📊 Risk Level")
    st.progress(float(prob))

    # =========================
    # BUSINESS INSIGHTS
    # =========================
    st.subheader("🧠 AI Insights")

    if prob > 0.7:
        st.error("🚨 Immediate Action Required: Offer discounts, loyalty plans.")
    elif prob > 0.4:
        st.warning("⚡ Moderate Risk: Engage with offers & communication.")
    else:
        st.success("✅ Customer Stable: Opportunity for upselling.")

    # =========================
    # EXTRA VISUAL INSIGHTS
    # =========================
    st.subheader("📈 Behavioral Indicators")

    risk_factors = {
        "Low Tenure": 1 if tenure < 12 else 0,
        "High Charges": 1 if monthly > 80 else 0,
        "Month Contract": 1 if contract == "Month-to-month" else 0
    }

    fig3 = px.bar(
        x=list(risk_factors.keys()),
        y=list(risk_factors.values()),
        color=list(risk_factors.values()),
        color_continuous_scale=["green", "red"]
    )
    st.plotly_chart(fig3, use_container_width=True)