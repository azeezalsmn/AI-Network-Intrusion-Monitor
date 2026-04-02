# Network Anomaly Detection & Topology Mapping

An end-to-end SIEM pipeline bridging wave physics and network intelligence. This system processes 100k+ network logs via Python, identifies threats with Isolation Forest ML, and maps the "blast radius" onto a dynamic infrastructure landscape.

## Implementation Workflow

### 1. Feature Engineering & Modeling (Python)
* **Pre-processing:** Cleaned 100,000+ records of raw network flows using Pandas/NumPy.
* **Model:** Implemented **Isolation Forest** (unsupervised learning) to identify outliers and generate a normalized `anomaly_score`.

### 2. Forensic Visualization (Elastic Stack)
* **Ingestion:** Configured custom index mapping in **Elasticsearch** for time-series telemetry.
* **Analysis:** Developed **Kibana** dashboards for attack profiling (DoS, Portscanning) and real-time incident drill-downs.
![Network Dashboard](DOCUMENTATIONS%20&%20ASSETS/DOCUMENTATION%201.png)

### 3. Infrastructure Topology Mapping (New)
* **Visualization:** Engineered an interactive graph using **NetworkX** and **Plotly** to map AI-detected anomalies to physical/logical nodes.
* **Impact:** Enables SOC analysts to visualize network segmentation and isolate compromised segments (e.g., IoT gateways or Edge routers) before lateral movement occurs.

![Network Topology](DOCUMENTATIONS%20&%20ASSETS/TOPOLOGY.png)
---

## Technical Stack
* **Languages:** Python (Scikit-Learn, NetworkX, Plotly)
* **Infrastructure:** Elasticsearch, Kibana (Elastic Stack)
* **Domain:** Network Security, eLORAN Navigation, Signal Propagation

## About the Author
**Azeeza Agrippina Lesmana** | Telecommunication Engineering @ ITS | IISMA Scholar @ UniPisa | INSPIRASI-NTU Alumna  
*Special interests include physical infrastructure and digital intelligence.*
