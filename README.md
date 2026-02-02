🛡️ AI-Based Network Intrusion Detection System (NIDS)

An AI-powered Network Intrusion Detection System that uses Machine Learning (Random Forest) and Generative AI (Grok) to detect and explain DDoS attacks from real network traffic data.
Built as a student cybersecurity project with strong relevance to SOC Analyst and Blue Team roles.

📌 Project Overview

Traditional NIDS tools can detect malicious traffic but often fail to explain why an alert was triggered.
This project enhances intrusion detection by combining:

Machine learning–based attack detection

Generative AI–based reasoning and explanation

Interactive SOC-style packet analysis

The system classifies network packets as BENIGN or DDoS and optionally generates human-readable explanations using an LLM.

## 📸 Project Dashboard Preview

<p align="center">
  <img src="images/nids-dashboard.png" alt="AI-Based NIDS Dashboard" width="900">
</p>

✨ Key Features

🧠 Random Forest–based intrusion detection

🧪 Real-world dataset (CIC-IDS2017 – DDoS traffic)

🤖 Generative AI explanations using Grok (optional)

📊 SOC-style random packet simulation

🌐 Interactive Streamlit web application

🎓 Beginner-friendly and educational

🏗️ Architecture (High Level)

Network traffic dataset loaded

Feature preprocessing and train/test split

Random Forest model training

Packet-level prediction (BENIGN / DDoS)

Optional AI explanation using LLM

Results displayed via Streamlit UI

🚀 Getting Started
Clone the Repository
git clone https://github.com/your-username/ai-nids-project.git
cd ai-nids-project

Install Dependencies
pip install -r requirements.txt

Run the Application
streamlit run app.py

🧪 How to Use

(Optional) Enter your Grok API key in the sidebar

Click Train AI Model to train the classifier

Click Simulate Random Packet

View:

Prediction result: BENIGN or DDoS

Model confidence

AI-generated explanation (if enabled)

📂 Project Structure
├── app.py
├── requirements.txt
├── Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
└── README.md

🛠️ Technologies Used

Python

Streamlit

Scikit-learn

Pandas

NumPy

Random Forest Classifier

Generative AI (Grok API)

📈 Use Cases

SOC Analyst training project

Cybersecurity academic submission

AI + Security demonstration

Blue Team learning lab

Resume / GitHub portfolio project

🎯 Learning Outcomes

Understand intrusion detection workflows

Apply machine learning to network security

Interpret network traffic–based attacks

Use LLMs to enhance SOC investigations

🚧 Future Improvements

Multi-attack classification (PortScan, Brute Force, Botnet)

Live packet capture integration

Model performance dashboard

MITRE ATT&CK technique mapping

SIEM integration (Splunk / Sentinel style)

⚠️ Disclaimer

This project is intended strictly for educational and research purposes and is not suitable for production deployment.