import streamlit as st

st.set_page_config(page_title="Reality Shield", layout="wide")

st.title("🛡️ Reality Shield")
st.caption("MindGuard • EchoTrace • TruthLens")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(
    ["🧠 MindGuard", "🔍 EchoTrace", "🧪 TruthLens"]
)

# ---------------- MindGuard ----------------
with tab1:
    st.subheader("🧠 MindGuard")
    text = st.text_area("Enter content to analyze", height=150)

    if st.button("Analyze Content"):
        if text.strip() == "":
            st.warning("Please enter some text.")
        else:
            st.success("Content analyzed successfully.")
            st.write("⚠️ This is a placeholder result.")

# ---------------- EchoTrace ----------------
with tab2:
    st.subheader("🔍 EchoTrace")
    source = st.text_input("Enter source URL or origin")

    if st.button("Trace Source"):
        if source.strip() == "":
            st.warning("Please enter a source.")
        else:
            st.success("Source traced successfully.")
            st.write("🔗 Origin tracing result (demo).")

# ---------------- TruthLens ----------------
with tab3:
    st.subheader("🧪 TruthLens")
    claim = st.text_area("Enter a claim to verify", height=150)

    if st.button("Verify Claim"):
        if claim.strip() == "":
            st.warning("Please enter a claim.")
        else:
            st.success("Claim verified successfully.")
            st.write("✅ Credibility score: 75% (demo)")
