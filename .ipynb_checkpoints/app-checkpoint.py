import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("mental_stress_model.pkl")

# Page config
st.set_page_config(
    page_title="Mental Stress Analyzer",
    page_icon="🧠",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}
.stButton>button {
    background-color: #6f42c1;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
}
.result-box {
    padding: 20px;
    border-radius: 10px;
    background-color: #ffffff;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
.footer {
    text-align: center;
    color: gray;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🧠 Mental Stress Pattern Analyzer")
st.caption("AI-powered stress detection using lifestyle patterns")

st.divider()

# Sidebar inputs
st.sidebar.header("🔍 Enter Your Details")

sleep = st.sidebar.slider("🛌 Sleep Hours", 0, 12, 6)
screen = st.sidebar.slider("📱 Screen Time (hours)", 0, 12, 5)
work = st.sidebar.slider("💼 Work Hours", 0, 12, 8)
mood = st.sidebar.slider("😊 Mood Level (0 = Worst, 3 = Best)", 0, 3, 2)
exercise = st.sidebar.slider("🏃 Exercise Minutes", 0, 120, 20)

# Main action
if st.button("🚀 Analyze Stress Level"):
    data = np.array([[sleep, screen, work, mood, exercise]])
    prediction = model.predict(data)[0]

    stress_map = {
        0: ("No Stress 😊", "Maintain your healthy routine."),
        1: ("Low Stress 🙂", "Good balance, stay consistent."),
        2: ("Moderate Stress 😐", "Consider relaxation and breaks."),
        3: ("High Stress 😟", "Take rest, reduce screen time, seek support.")
    }

    label, advice = stress_map[prediction]

    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.subheader("📊 Stress Analysis Result")
    st.success(label)
    st.write("💡 Recommendation:")
    st.info(advice)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.divider()
st.markdown(
    '<div class="footer">Developed as part of AICTE AI-ML Internship Project</div>',
    unsafe_allow_html=True
)