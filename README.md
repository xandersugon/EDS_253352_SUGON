# 🛰️ Programmatic Anomaly Analysis and Statistical Profiling of Soil Moisture Active Passive (SMAP) Satellite Telemetry Using an Object-Oriented Engineering Data Pipeline

An object-oriented data engineering pipeline designed to ingest, clean, and profile Soil Moisture Active Passive (SMAP) satellite telemetry. This architecture automates anomaly detection, isolates data stream variances, and generates statistical diagnostics to ensure telemetry integrity.

## 📁 Repository Structure
* **data/**: Ingested telemetry datasets (e.g., `dataset_cleaned.csv`).
* **outputs/**: Generated statistical profiles, static histograms, boxplots, and interactive telemetry time-trend visualizations.
* **main.py**: Core executable deploying the object-oriented data processing and anomaly detection pipeline.
* **.gitignore**: Explicitly configured to exclude the local environment (`.venv/`) and tracking cache.

## 🚀 Getting Started

### 1. Environment Activation
Activate the dedicated virtual environment within your terminal:
```powershell
.\venv\Scripts\Activate.ps1