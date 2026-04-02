# AI-Network-Intrusion-Monitor
End-to-end SIEM pipeline: 100k+ network logs processed via Python, analyzed with Isolation Forest ML for anomaly detection, and visualized on an Elastic/Kibana dashboard for real-time threat forensics.

# 🛡️ AI-Driven Network Intrusion Detection System (NIDS)
### Real-Time Anomaly Detection with Isolation Forest & Elastic Stack

![Network Security Dashboard](YOUR_SCREENSHOT_LINK_HERE)

## 📌 Project Overview
This project demonstrates a production-grade **Security Information and Event Management (SIEM)** pipeline. It processes over 100,000 raw network logs, applies unsupervised **Machine Learning** to score anomalies, and visualizes threats for a Security Operations Center (SOC) environment.

Developed as part of a technical portfolio for **Telecommunication Engineering**, this system reduces "alert fatigue" by highlighting high-risk traffic patterns (DoS, Portscan) using AI.

---

## 🚀 Technical Architecture
The pipeline follows a modern data engineering workflow:
1. **Data Engineering:** Pre-processing the CIC-IDS dataset (100k+ rows) using **Python & Pandas**.
2. **Machine Learning:** Implementing an **Isolation Forest** model to calculate `anomaly_score` (0.0 to 1.0).
3. **Data Ingestion:** Indexing enriched JSON data into **Elasticsearch** via Elastic Cloud.
4. **Visualization:** Designing a forensic **Kibana Dashboard** for threat distribution and temporal analysis.



---

## 📊 Dashboard Features
* **Attack Distribution (Pie Chart):** High-level breakdown of Benign vs. Malicious traffic (DoS Hulk, Slowloris, etc.).
* **Anomaly Timeline (Area Chart):** Real-time visualization of when the AI model flags suspicious behavior.
* **Forensic Table:** Detailed raw log view including `@timestamp`, `destination_port`, and `is_anomaly` flags.

---

## 🛠️ Tools & Technologies
* **Languages:** Python 3.10
* **ML Libraries:** Scikit-Learn, NumPy
* **Platform:** Elastic Stack (Elasticsearch 8.x, Kibana)
* **Dataset:** CIC-IDS2017 (Network Traffic)

---

## 💡 Key Insights
* **Pattern Recognition:** Successfully identified Portscan attempts targeting specific service ports (80, 443).
* **AI Accuracy:** The Isolation Forest model effectively separated high-volume DoS attacks from normal background traffic with minimal false positives.

---

## 👤 About the Author
**Your Name** *Telecommunication Engineering @ Sepuluh Nopember Institute of Technology (ITS)* *IISMA Scholar | University of Pisa* [LinkedIn](YOUR_LINKEDIN_URL) | [Portfolio](YOUR_WEBSITE_URL)
