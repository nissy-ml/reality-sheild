import streamlit as st
import random

st.set_page_config(page_title="Reality Shield", layout="wide")

st.title("🛡️ Reality Shield")
st.caption("MindGuard • EchoTrace • TruthLens")
st.markdown("---")

tab1, tab2, tab3 = st.tabs(
    ["🧠 MindGuard", "🔍 EchoTrace", "🧪 TruthLens"]
)

# ================= MindGuard =================
with tab1:
    st.subheader("🧠 MindGuard – Stress & Burnout Analysis")
    text = st.text_area("Describe how you are feeling", height=150)

    if st.button("Analyze Mental State"):
        if text.strip() == "":
            st.warning("Please enter your thoughts.")
        else:
            keywords = ["stress", "tired", "exhausted", "burnout", "pressure", "anxious"]
            score = sum(1 for k in keywords if k in text.lower())

            stress = min(20 + score * 15, 95)
            burnout = min(stress - 5, 90)

            st.write(f"🔴 **Stress Level:** {stress}%")
            st.write(f"🟠 **Burnout Risk:** {burnout}%")

            if stress > 70:
                st.error("High stress detected")
                st.info("💡 Suggestion: Take rest, reduce workload, talk to someone you trust.")
            elif stress > 40:
                st.warning("Moderate stress detected")
                st.info("💡 Suggestion: Take breaks, sleep well, manage time better.")
            else:
                st.success("Low stress detected")
                st.info("💡 Suggestion: Maintain healthy routines.")

# ================= EchoTrace =================
with tab2:
    st.subheader("🔍 EchoTrace – Source Reliability Check")
    source = st.text_input("Enter news source / URL / platform")

    if st.button("Analyze Source"):
        if source.strip() == "":
            st.warning("Please enter a source.")
        else:
            reliability = random.randint(40, 90)

            st.write(f"📊 **Source Reliability:** {reliability}%")

            if reliability < 50:
                st.error("Low reliability source")
                st.info("💡 Suggestion: Cross-check with trusted platforms.")
            elif reliability < 75:
                st.warning("Moderate reliability source")
                st.info("💡 Suggestion: Verify before sharing.")
            else:
                st.success("High reliability source")
                st.info("💡 Suggestion: Source appears trustworthy.")

# ================= TruthLens =================
with tab3:
    st.subheader("🧪 TruthLens – Claim Verification")
    claim = st.text_area("Enter a claim to verify", height=150)

    if st.button("Verify Claim"):
        if claim.strip() == "":
            st.warning("Please enter a claim.")
        else:
            credibility = random.randint(45, 95)

            st.write(f"✅ **Credibility Score:** {credibility}%")

            if credibility < 50:
                st.error("Likely false or misleading")
                st.info("💡 Suggestion: Do not share without verification.")
            elif credibility < 75:
                st.warning("Partially true or unclear")
                st.info("💡 Suggestion: Look for reliable references.")
            else:
                st.success("Likely true")
                st.info("💡 Suggestion: Information appears reliable.")
