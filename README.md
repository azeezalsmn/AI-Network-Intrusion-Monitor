# AI-Network-Intrusion-Monitor
End-to-end SIEM pipeline: 100k+ network logs processed via Python, analyzed with Isolation Forest ML for anomaly detection, and visualized on an Elastic/Kibana dashboard for real-time threat forensics.

# Network Intrusion Monitoring with ML-Based Anomaly Scoring
**Automated NIDS pipeline using Elastic Stack and Scikit-Learn for high-volume traffic analysis.**

![Network Security Dashboard](DOCUMENTATIONS)

## Technical Overview
This project addresses the challenge of identifying malicious patterns within high-volume network traffic. Using a subset of the **CIC-IDS2017 dataset** (100,000+ records), I developed a pipeline that cleans raw network flows, calculates anomaly scores using an unsupervised model, and provides a forensic interface for security analysts.

## Implementation Workflow

### 1. Feature Engineering & Modeling (Python)
* **Pre-processing:** Cleaned and normalized flow features including Source/Destination Ports, Flow Duration, and Packet Length using **Pandas** and **NumPy**.
* **Model:** Implemented **Isolation Forest** (unsupervised learning) to identify outliers and generate a normalized `anomaly_score`.
* **Output:** Generated binary `is_anomaly` flags to streamline threat prioritization.

### 2. Data Infrastructure (Elasticsearch)
* **Ingestion:** Configured custom index mapping in **Elasticsearch** to handle time-series network telemetry.
* **Optimization:** Tuned index settings for 100k+ documents to ensure low-latency filtering and real-time dashboard updates.

### 3. Forensic Visualization (Kibana)
* **Telemetry Timeline:** Time-series analysis correlating traffic spikes with AI-generated anomaly scores.
* **Attack Profiling:** Distribution analysis of identified threats including DoS Hulk, Slowloris, and Portscanning.
* **Incident Drill-down:** Integrated a raw document table for investigating specific service ports (e.g., Port 80/443) targeted during detected anomalies.

## Technical Stack & Competencies
* **Languages:** Python (Scikit-Learn, Pandas, NumPy)
* **Infrastructure:** Elasticsearch, Kibana (Elastic Stack)
* **Domain Knowledge:** Network Security, Telecommunications, Data-driven Optimization

## Project Impact
By automating anomaly detection, this system enables a Security Operations Center (SOC) to prioritize high-risk traffic, significantly reducing the manual effort required for log review and improving response times to network-level threats.

---

## About the Author
**Azeeza Agrippina Lesmana**
* **Telecommunication Engineering** at Sepuluh Nopember Institute of Technology (ITS).
* **Research Intern** for eLORAN Signal Propagation & Navigation Systems Engineering in collaboration with **Gauss Research Foundation, Netherlands**.
* **IISMA Government Scholar** at Università di Pisa, Italy (Engineering Dept.).
* **Head Laboratory Assistant** at the Antenna and Propagation Laboratory - ITS.

[LinkedIn](https://linkedin.com/in/azeezalsmn) | azeezalsmn@gmail.com
