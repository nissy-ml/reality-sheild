import streamlit as st
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Reality Shield", layout="wide")

# ---------------- MOBILE UI CSS ----------------
st.markdown("""
<style>
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}
textarea, input {
    font-size: 16px !important;
}
button {
    width: 100%;
    font-size: 18px;
}
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- SPEEDOMETER FUNCTION ----------------
def speedometer(title, value):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "black"},
                "steps": [
                    {"range": [0, 40], "color": "#8fd19e"},
                    {"range": [40, 70], "color": "#ffe066"},
                    {"range": [70, 100], "color": "#ff6b6b"},
                ],
            }
        )
    )
    st.plotly_chart(fig, use_container_width=True)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align:center;'>🛡️ Reality Shield</h1>
    <p style='text-align:center; color:gray;'>
    MindGuard • EchoTrace • TruthLens
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["🧠 MindGuard", "🔍 EchoTrace", "🧪 TruthLens"])

# ===================== MINDGUARD =====================
with tab1:
    st.subheader("🧠 MindGuard – Stress & Burnout Analyzer")

    text = st.text_area(
        "Describe how you are feeling",
        height=160,
        placeholder="Example: I feel exhausted, anxious, and overwhelmed with studies"
    )

    if st.button("Analyze Mental State", use_container_width=True):
        if text.strip() == "":
            st.warning("Please enter some text.")
        else:
            keywords = [
                "stress", "tired", "exhausted", "burnout",
                "pressure", "anxious", "overwhelmed", "panic"
            ]
            score = sum(1 for k in keywords if k in text.lower())

            stress = min(30 + score * 10, 95)
            burnout = max(stress - 10, 0)

            speedometer("Stress Level (%)", stress)
            speedometer("Burnout Risk (%)", burnout)

            if stress >= 70:
                st.error("High stress detected")
                st.info("Suggestion: Take rest, reduce workload, talk to someone you trust.")
            elif stress >= 40:
                st.warning("Moderate stress detected")
                st.info("Suggestion: Take breaks, sleep well, plan tasks.")
            else:
                st.success("Low stress detected")
                st.info("Suggestion: Maintain healthy habits.")

# ===================== ECHOTRACE =====================
with tab2:
    st.subheader("🔍 EchoTrace – Source Reliability Analyzer")

    source = st.text_input(
        "Enter news source / platform",
        placeholder="Example: WhatsApp forward, unknown website"
    )

    if st.button("Analyze Source", use_container_width=True):
        if source.strip() == "":
            st.warning("Please enter a source.")
        else:
            risky_sources = ["whatsapp", "forward", "telegram", "unknown"]
            risk = sum(1 for r in risky_sources if r in source.lower())

            reliability = max(85 - risk * 20, 30)

            speedometer("Source Reliability (%)", reliability)

            if reliability < 50:
                st.error("Low reliability source")
                st.info("Suggestion: Cross-check with trusted news websites.")
            elif reliability < 75:
                st.warning("Moderate reliability source")
                st.info("Suggestion: Verify information before sharing.")
            else:
                st.success("High reliability source")
                st.info("Suggestion: Source appears trustworthy.")

# ===================== TRUTHLENS =====================
with tab3:
    st.subheader("🧪 TruthLens – Claim Credibility Checker")

    claim = st.text_area(
        "Enter a claim to verify",
        height=160,
        placeholder="Example: Drinking hot water cures viral infections"
    )

    if st.button("Verify Claim", use_container_width=True):
        if claim.strip() == "":
            st.warning("Please enter a claim.")
        else:
            flags = ["always", "never", "100%", "guaranteed", "instantly"]
            flag_score = sum(1 for f in flags if f in claim.lower())

            credibility = max(90 - flag_score * 18, 35)

            speedometer("Credibility Score (%)", credibility)

            if credibility < 50:
                st.error("Likely false or misleading")
                st.info("Suggestion: Do not share without verification.")
            elif credibility < 75:
                st.warning("Partially true or unclear")
                st.info("Suggestion: Check reliable references.")
            else:
                st.success("Likely true")
                st.info("Suggestion: Information appears reliable.")

st.markdown("---")
st.caption("⚠️ Disclaimer: This tool is for awareness and educational purposes only.")
