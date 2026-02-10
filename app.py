import streamlit as st
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Reality Shield",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- MOBILE-FIRST + COLORFUL CSS ----------------
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

h1, h2, h3 {
    text-align: center;
}

textarea, input {
    font-size: 16px !important;
    border-radius: 10px;
    border: 2px solid #0d3b66;
    padding: 0.5rem;
}

button {
    width: 100% !important;
    font-size: 18px !important;
    padding: 0.6rem !important;
    border-radius: 12px !important;
    color: white !important;
}

div[data-testid="stMetric"] {
    text-align: center;
}

@media (max-width: 768px) {
    .block-container {
        padding-left: 0.8rem;
        padding-right: 0.8rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- SPEEDOMETER WITH MODULE COLORS ----------------
def speedometer(title, value, module="default"):
    colors = {
        "mind": ["#8fd19e", "#b0e57c", "#22aa33"],      # green shades
        "echo": ["#fff59d", "#ffe066", "#ffb300"],      # yellow shades
        "truth": ["#ff8a80", "#ff6b6b", "#d32f2f"],     # red shades
        "default": ["#9be7a1", "#ffe066", "#ff6b6b"]    # default
    }
    step_colors = colors.get(module, colors["default"])
    
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": step_colors[2]},
                "steps": [
                    {"range": [0, 40], "color": step_colors[0]},
                    {"range": [40, 70], "color": step_colors[1]},
                    {"range": [70, 100], "color": step_colors[2]},
                ],
                "threshold": {
                    "line": {"color": "black", "width": 4},
                    "thickness": 0.75,
                    "value": value
                }
            }
        )
    )
    st.plotly_chart(fig, use_container_width=True)

# ---------------- HEADER ----------------
st.markdown("""
<div style="background: linear-gradient(90deg, #8fd19e, #ffe066, #ff6b6b); 
            padding: 1.5rem; border-radius: 10px; text-align:center; color:white; font-size:2.2rem; font-weight:bold;">
🛡️ Reality Shield
</div>
<p style='text-align:center; color:#555;'>MindGuard • EchoTrace • TruthLens</p>
""", unsafe_allow_html=True)

st.divider()

tab1, tab2, tab3 = st.tabs([
    "🧠 MindGuard",
    "🔍 EchoTrace",
    "🧪 TruthLens"
])

# ================= MINDGUARD =================
with tab1:
    st.subheader("Stress & Burnout Analyzer")

    text = st.text_area(
        "How are you feeling?",
        height=150,
        placeholder="Example: I feel stressed, tired and overwhelmed with studies"
    )

    if st.button("Analyze Mental State"):
        if not text.strip():
            st.warning("Please enter some text.")
        else:
            keywords = [
                "stress", "tired", "exhausted", "burnout",
                "pressure", "anxious", "overwhelmed", "panic"
            ]
            score = sum(1 for k in keywords if k in text.lower())

            stress = min(30 + score * 10, 95)
            burnout = max(stress - 10, 0)

            speedometer("Stress Level (%)", stress, module="mind")
            speedometer("Burnout Risk (%)", burnout, module="mind")

            if stress >= 70:
                st.error("High stress detected")
                st.info("Suggestion: Take rest, reduce workload, talk to someone.")
            elif stress >= 40:
                st.warning("Moderate stress detected")
                st.info("Suggestion: Take breaks and manage time well.")
            else:
                st.success("Low stress detected")
                st.info("Suggestion: Maintain healthy habits.")

# ================= ECHOTRACE =================
with tab2:
    st.subheader("Source Reliability Checker")

    source = st.text_input(
        "Enter source or platform",
        placeholder="Example: WhatsApp forward"
    )

    if st.button("Analyze Source"):
        if not source.strip():
            st.warning("Please enter a source.")
        else:
            risky = ["whatsapp", "forward", "telegram", "unknown"]
            risk_score = sum(1 for r in risky if r in source.lower())

            reliability = max(85 - risk_score * 20, 30)

            speedometer("Source Reliability (%)", reliability, module="echo")

            if reliability < 50:
                st.error("Low reliability source")
                st.info("Suggestion: Verify with trusted news sites.")
            elif reliability < 75:
                st.warning("Moderate reliability")
                st.info("Suggestion: Cross-check before sharing.")
            else:
                st.success("High reliability source")
                st.info("Suggestion: Source appears trustworthy.")

# ================= TRUTHLENS =================
with tab3:
    st.subheader("Claim Credibility Checker")

    claim = st.text_area(
        "Enter a claim",
        height=150,
        placeholder="Example: This method guarantees 100% instant results"
    )

    if st.button("Verify Claim"):
        if not claim.strip():
            st.warning("Please enter a claim.")
        else:
            flags = ["always", "never", "100%", "guaranteed", "instantly"]
            flag_score = sum(1 for f in flags if f in claim.lower())

            credibility = max(90 - flag_score * 18, 35)

            speedometer("Credibility Score (%)", credibility, module="truth")

            if credibility < 50:
                st.error("Likely false or misleading")
                st.info("Suggestion: Do not share without verification.")
            elif credibility < 75:
                st.warning("Partially true or unclear")
                st.info("Suggestion: Check reliable references.")
            else:
                st.success("Likely true")
                st.info("Suggestion: Information appears reliable.")

st.divider()
st.caption("⚠️ For awareness and educational purposes only.")
