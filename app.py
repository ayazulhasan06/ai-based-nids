import streamlit as st
import pandas as pd
import numpy as np
import os
from groq import Groq

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="AI-Based Network Intrusion Detection System",
    layout="wide"
)

st.title("🛡️ AI-Based Network Intrusion Detection System")
st.markdown(
    "**Student Project**: This application uses statistical AI techniques "
    "to analyze real network traffic and detect potential DDoS attacks."
)

# ---------------- DATASET ----------------
DATA_FILE = "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"

FEATURES = [
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Length of Fwd Packets",
    "Fwd Packet Length Max",
    "Flow IAT Mean",
    "Flow IAT Std",
    "Flow Packets/s",
]

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE, nrows=20000)
    df.columns = df.columns.str.strip()
    df = df[FEATURES + ["Label"]]
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)
    return df

if not os.path.exists(DATA_FILE):
    st.error("Dataset not found. Place the CSV file in the same folder as app.py.")
    st.stop()

df = load_data()
st.success(f"Dataset loaded successfully ({len(df)} rows)")

# ---------------- AI TRAINING (STATISTICAL MODEL) ----------------
@st.cache_data
def train_ai_model(df):
    stats = {}
    for col in FEATURES:
        stats[col] = {
            "mean": df[col].mean(),
            "std": df[col].std()
        }
    return stats

ai_stats = train_ai_model(df)

# ---------------- AI PREDICTION ----------------
def ai_predict(packet, stats):
    anomaly_score = 0

    for col in FEATURES:
        z_score = abs(packet[col] - stats[col]["mean"]) / stats[col]["std"]
        if z_score > 2:
            anomaly_score += 1

    confidence = anomaly_score / len(FEATURES)

    if confidence > 0.25:
        return "DDoS Attack", confidence
    else:
        return "Benign", confidence

# ---------------- SIDEBAR ----------------
st.sidebar.header("🤖 AI Explanation (Optional)")
groq_api_key = st.sidebar.text_input("Groq API Key", type="password")

# ---------------- DASHBOARD ----------------
st.header("📊 Threat Analysis Dashboard")
st.info("Analyze a real network packet using AI-based anomaly detection.")

if st.button("🎲 Analyze Random Network Packet"):
    row = df.sample(1).iloc[0]
    packet = row[FEATURES]

    prediction, confidence = ai_predict(packet, ai_stats)

    st.session_state.packet = packet
    st.session_state.prediction = prediction
    st.session_state.confidence = confidence
    st.session_state.true_label = row["Label"]

# ---------------- DISPLAY RESULTS ----------------
if "packet" in st.session_state:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📦 Packet Features")
        st.dataframe(
            st.session_state.packet.to_frame("Value"),
            use_container_width=True
        )

    with col2:
        st.subheader("🧠 AI Detection Result")

        if st.session_state.prediction == "Benign":
            st.success("✅ STATUS: SAFE (BENIGN)")
        else:
            st.error("🚨 STATUS: ATTACK DETECTED (DDoS)")

        st.metric(
            "AI Confidence",
            f"{st.session_state.confidence * 100:.2f}%"
        )
        st.caption(f"Ground Truth Label: {st.session_state.true_label}")

# ---------------- AI EXPLANATION ----------------
st.markdown("---")
st.subheader("🤖 AI Explanation")

if st.button("Explain with AI"):
    if not groq_api_key:
        st.warning("Please enter your Groq API key in the sidebar.")
    else:
        client = Groq(api_key=groq_api_key)

        prompt = f"""
        Explain why this network packet was classified as
        {st.session_state.prediction}.
        Keep the explanation simple and student-friendly.

        Packet details:
        {st.session_state.packet.to_string()}
        """

        with st.spinner("AI analyzing..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5
            )

        st.info(response.choices[0].message.content)
