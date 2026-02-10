import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Reality Shield",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- MOBILE-FIRST + COLORFUL CSS ----------------
st.markdown("""
<style>
.block-container {padding: 1rem;}
h1, h2, h3 {text-align: center;}
textarea, input {font-size: 16px !important; border-radius:10px; border:2px solid #0d3b66; padding:0.5rem;}
button {width:100% !important; font-size:18px !important; padding:0.6rem !important; border-radius:12px !important; color:white !important;}
div[data-testid="stMetric"] {text-align:center;}
.stExpander {background-color:#f0f4f8 !important; border-radius:8px; padding:0.5rem;}
@media (max-width:768px){.block-container {padding-left:0.8rem; padding-right:0.8rem;}}
</style>
""", unsafe_allow_html=True)

# ---------------- SPEEDOMETER ----------------
def speedometer(title, value, module="default"):
    colors = {
        "mind": ["#8fd19e", "#b0e57c", "#22aa33"],
        "echo": ["#fff59d", "#ffe066", "#ffb300"],
        "truth": ["#ff8a80", "#ff6b6b", "#d32f2f"],
        "default": ["#9be7a1", "#ffe066", "#ff6b6b"]
    }
    step_colors = colors.get(module, colors["default"])
    
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title},
            gauge={
                "axis": {"range":[0,100]},
                "bar": {"color": step_colors[2]},
                "steps":[
                    {"range":[0,40],"color":step_colors[0]},
                    {"range":[40,70],"color":step_colors[1]},
                    {"range":[70,100],"color":step_colors[2]},
                ],
                "threshold":{"line":{"color":"black","width":4},"thickness":0.75,"value":value}
            }
        )
    )
    st.plotly_chart(fig, use_container_width=True)

# ---------------- HEADER ----------------
st.markdown("""
<div style="background: linear-gradient(90deg, #8fd19e, #ffe066, #ff6b6b); 
            padding:1.5rem; border-radius:10px; text-align:center; color:white; font-size:2.2rem; font-weight:bold;">
🛡️ Reality Shield
</div>
<p style='text-align:center; color:#555;'>MindGuard • EchoTrace • TruthLens</p>
""", unsafe_allow_html=True)

st.divider()
tab1, tab2, tab3 = st.tabs(["🧠 MindGuard","🔍 EchoTrace","🧪 TruthLens"])

# ================= UTILITY FOR HISTORY =================
if "history" not in st.session_state:
    st.session_state.history = {"MindGuard":[],"EchoTrace":[],"TruthLens":[]}

def add_history(module, description, value):
    st.session_state.history[module].append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "description": description,
        "value": value
    })

def display_history(module):
    if st.session_state.history[module]:
        st.subheader("📈 Session History")
        for h in reversed(st.session_state.history[module][-5:]):  # last 5 entries
            st.markdown(f"**{h['time']}** – {h['description']}: {h['value']}%")

# ================= MINDGUARD =================
with tab1:
    st.subheader("Stress & Burnout Analyzer")
    text = st.text_area("How are you feeling?", height=150,
                        placeholder="Example: I feel stressed, tired and overwhelmed")
    
    if st.button("Analyze Mental State"):
        if not text.strip():
            st.warning("Please enter some text.")
        else:
            keywords = ["stress","tired","exhausted","burnout","pressure","anxious","overwhelmed","panic"]
            score = sum(1 for k in keywords if k in text.lower())
            stress = min(30 + score*10, 95)
            burnout = max(stress - 10,0)
            
            speedometer("Stress Level (%)", stress, module="mind")
            speedometer("Burnout Risk (%)", burnout, module="mind")
            
            # --- Interactive suggestions ---
            if stress>=70:
                with st.expander("High stress detected – Click for guidance"):
                    st.info("🌱 Pause and breathe deeply. Recognize your efforts. Small mindful steps today reshape tomorrow.")
            elif stress>=40:
                with st.expander("Moderate stress detected – Click for guidance"):
                    st.info("🌿 Notice tension but you are in control. Plan, prioritize, and allow calm moments.")
            else:
                with st.expander("Low stress detected – Click for guidance"):
                    st.info("🌟 Great balance! Stay curious and nurture healthy habits.")
            
            add_history("MindGuard","Stress & Burnout",stress)

    display_history("MindGuard")

# ================= ECHOTRACE =================
with tab2:
    st.subheader("Source Reliability Checker")
    source = st.text_input("Enter source or platform",placeholder="Example: WhatsApp forward")
    
    if st.button("Analyze Source"):
        if not source.strip():
            st.warning("Please enter a source.")
        else:
            risky = ["whatsapp","forward","telegram","unknown"]
            risk_score = sum(1 for r in risky if r in source.lower())
            reliability = max(85 - risk_score*20,30)
            
            speedometer("Source Reliability (%)", reliability, module="echo")
            
            if reliability<50:
                with st.expander("Low reliability source – Click for advice"):
                    st.info("🔍 Pause and reflect before trusting. Seek verified references and cross-check facts.")
            elif reliability<75:
                with st.expander("Moderate reliability – Click for advice"):
                    st.info("⚡ Be mindful. Question, explore, and form your own informed opinion.")
            else:
                with st.expander("High reliability – Click for advice"):
                    st.info("✅ Appears trustworthy. Stay aware and keep critical thinking active.")
            
            add_history("EchoTrace","Source Reliability",reliability)

    display_history("EchoTrace")

# ================= TRUTHLENS =================
with tab3:
    st.subheader("Claim Credibility Checker")
    claim = st.text_area("Enter a claim",height=150,placeholder="Example: This method guarantees 100% instant results")
    
    if st.button("Verify Claim"):
        if not claim.strip():
            st.warning("Please enter a claim.")
        else:
            flags = ["always","never","100%","guaranteed","instantly"]
            flag_score = sum(1 for f in flags if f in claim.lower())
            credibility = max(90 - flag_score*18,35)
            
            speedometer("Credibility Score (%)", credibility, module="truth")
            
            if credibility<50:
                with st.expander("Likely false or misleading – Click for advice"):
                    st.info("⚠️ Pause before accepting/sharing. Question assumptions, explore evidence, and act consciously.")
            elif credibility<75:
                with st.expander("Partially true or unclear – Click for advice"):
                    st.info("💡 Approach carefully. Investigate, reflect, and stay open to learning.")
            else:
                with st.expander("Likely true – Click for advice"):
                    st.info("🌟 Seems credible. Use insight responsibly and continue thoughtful analysis.")
            
            add_history("TruthLens","Claim Credibility",credibility)

    display_history("TruthLens")

st.divider()
st.caption("⚠️ For awareness, education, and personal insight purposes only.")
