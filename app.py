import streamlit as st
import random

st.set_page_config(page_title="Reality Shield", layout="wide")

# ---------- HEADER ----------
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

tab1, tab2, tab3 = st.tabs(
    ["🧠 MindGuard", "🔍 EchoTrace", "🧪 TruthLens"]
)

# ================= MINDGUARD =================
with tab1:
    st.subheader("🧠 MindGuard – Stress & Burnout Analyzer")

    text = st.text_area(
        "Describe how you are feeling",
        height=160,
        placeholder="Example: I feel exhausted, anxious, and overwhelmed with studies..."
    )

    if st.button("Analyze Mental State"):
        if text.strip() == "":
            st.warning("Please enter some text.")
        else:
            keywords = [
                "stress", "tired", "exhausted", "burnout",
                "pressure", "anxious", "overwhelmed", "panic"
            ]
            score = sum(1 for k in keywords if k in text.lower())

            stress = min(25 + score * 12, 95)
            burnout = min(stress - 10, 90)

            st.markdown("### 📊 Results")
            st.write(f"**Stress Level:** {stress}%")
            st.progress(stress/100)

            st.write(f"**Burnout Risk:** {burnout}%")
            st.progress(burnout/100)

            if stress > 70:
                st.error("High stress detected")
                st.info("💡 Suggestion: Take rest, reduce workload, talk to someone you trust.")
            elif stress > 40:
                st.warning("Moderate stress detected")
                st.info("💡 Suggestion: Take breaks, sleep well, plan tasks.")
            else:
                st.success("Low stress detected")
                st.info("💡 Suggestion: Maintain healthy habits.")

# ================= ECHOTRACE =================
with tab2:
    st.subheader("🔍 EchoTrace – Source Reliability Analyzer")

    source = st.text_input(
        "Enter news source / URL / platform",
        placeholder="Example: WhatsApp forward, unknown website, news portal"
    )

    if st.button("Analyze Source"):
        if source.strip() == "":
            st.warning("Please enter a source.")
        else:
            suspicious = ["whatsapp", "forward", "unknown", "telegram"]
            risk = sum(1 for s in suspicious if s in source.lower())

            reliability = max(85 - risk * 20, 30)

            st.markdown("### 📊 Results")
            st.write(f"**Source Reliability:** {reliability}%")
            st.progress(reliability/100)

            if reliability < 50:
                st.error("Low reliability source")
                st.info("💡 Suggestion: Cross-check with trusted news websites.")
            elif reliability < 75:
                st.warning("Moderate reliability source")
                st.info("💡 Suggestion: Verify information before sharing.")
            else:
                st.success("High reliability source")
                st.info("💡 Suggestion: Source appears trustworthy.")

# ================= TRUTHLENS =================
with tab3:
    st.subheader("🧪 TruthLens – Claim Credibility Checker")

    claim = st.text_area(
        "Enter a claim to verify",
        height=160,
        placeholder="Example: Drinking hot water cures viral infections"
    )

    if st.button("Verify Claim"):
        if claim.strip() == "":
            st.warning("Please enter a claim.")
        else:
            flags = ["always", "never", "100%", "guaranteed", "instantly"]
            flag_score = sum(1 for f in flags if f in claim.lower())

            credibility = max(90 - flag_score * 18, 35)

            st.markdown("### 📊 Results")
            st.write(f"**Credibility Score:** {credibility}%")
            st.progress(credibility/100)

            if credibility < 50:
                st.error("Likely false or misleading")
                st.info("💡 Suggestion: Do not share without verification.")
            elif credibility < 75:
                st.warning("Partially true or unclear")
                st.info("💡 Suggestion: Check reliable references.")
            else:
                st.success("Likely true")
                st.info("💡 Suggestion: Information appears reliable.")

st.markdown("---")
st.caption("⚠️ Disclaimer: This tool provides heuristic-based analysis for awareness, not medical or legal advice.")
