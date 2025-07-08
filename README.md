# 🏎️ Formula 1 2021 Grand Prix Winners — Cloud Data Pipeline & Visualization

This project showcases a complete end-to-end **data engineering + DevOps + BI visualization pipeline** based on the 2021 Formula 1 season 🏁.  
We combined **data transformation with Python**, **Azure Blob Storage for cloud hosting**, **GitHub Actions for CI/CD**, and **Power BI** for interactive insights into which driver conquered each Grand Prix.

Our goal?  
Build a project that not only delivers clean insights but does it like a pit crew — **fast, precise, and with zero engine failures** 🧑‍🔧⚙️

---

## 🔧 Tech Stack & Tools

[![Python](https://img.shields.io/badge/Python-Data%20Processing-yellow?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-%23150458?logo=pandas)](https://pandas.pydata.org/)
[![Azure](https://img.shields.io/badge/Azure-Blob%20Storage-blue?logo=microsoftazure)](https://azure.microsoft.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-blue?logo=githubactions)](https://github.com/features/actions)
[![Power BI](https://img.shields.io/badge/PowerBI-Visualization-F2C811?logo=powerbi)](https://powerbi.microsoft.com/)
[![CSV](https://img.shields.io/badge/Data-CSV-lightgrey?logo=csv)](https://www.kaggle.com/datasets/prathamsharma123/formula-1-fantasy-2021)

---
## 🚀 Project Workflow
Phase	Description
🏁 Data Ingestion	Sourced the Formula 1 Fantasy 2021 dataset from Kaggle
🛠️ Data Processing	Used Python (Pandas) to clean and reshape the data
🔁 CI/CD	GitHub Actions triggers pipeline on every push
☁️ Cloud Storage	Processed file uploaded to Azure Blob using SDK
📊 Visualization	Power BI Dashboard shows GP winners, driver trends, and race breakdowns

## 🚀 What This Project Does
Phase	Description
📦 Data Ingestion	Downloaded Formula 1 Fantasy 2021 dataset from Kaggle
⚙️ Data Processing	Python script (pandas) to clean and reshape the dataset
🔁 CI/CD	GitHub Actions pipeline auto-triggers transformation & upload to Azure
☁️ Cloud Storage	Output CSV stored in Azure Blob (Gen2) using Azure SDK
📊 Visualization	Power BI dashboard to display race-by-race Grand Prix winners

## 

## 📊 Power BI Dashboard Highlights
Built with Power BI Desktop, our dashboard includes:

🥇 Bar charts showing which driver won each Grand Prix

📈 Line charts of driver performance trends across the season

📌 Slicers to filter by driver or GP

🏆 Cards showing total races, unique winners, and top performers

🏎️ Note: Despite Max Verstappen and Lewis Hamilton battling it out on the track, in our dashboard, they battle in bar charts and slicers 😄
It’s like F1, but with less carbon emissions and more pandas 🐼

Data source - https://www.kaggle.com/datasets/prathamsharma123/formula-1-fantasy-2021?resource=download

## 🛡️ GitHub Actions CI/CD Flow
The workflow is defined in .github/workflows/data-pipeline.yml and includes:

Trigger on push

Set up Python & dependencies

Run scripts/transform.py

Upload to Azure Blob via SDK using GitHub Secrets

## 📌 How to Run This Project
Clone the repo & set up your Python environment

Add your Azure Blob credentials as GitHub Secrets:

AZURE_STORAGE_CONNECTION_STRING

Push changes to trigger CI/CD

View the file in Azure Blob → Load into Power BI via SAS URL


##🧪 CI/CD Pipeline Details
File: .github/workflows/data-pipeline.yml

✅ Triggered on push or commit

✅ Installs dependencies (pandas, azure-storage-blob)

✅ Runs transform.py to clean data

✅ Uploads processed data to Azure Blob (processed container)

✅ Secrets managed via GitHub Secrets

## 💡 Future Scope
Add live race data integration from F1 APIs 🛰️

Build an automatic refresh dashboard connected to Azure Blob

Integrate driver comparison analytics across seasons

## 👨‍👩‍👧 Group Contribution
This project was a full-team effort, developed with the passion of an F1 pit crew and the speed of a GitHub Action 🛠️⚡

Shivali —  Data pipeline commander 👨‍💻& project hype manager ☁️⚔️

Vaishali — Power BI dashboard & Python 

Adharsh — DevOps engineer & Azure storage 

Together, we turned laps of raw CSVs into beautiful dashboards, and managed not to crash into NullTypeError() on the last turn 🏎️💥

## 🏁 Final Words
This isn't just a project — it's a digital racetrack where:

Pandas do the pit stops

YAML handles the strategy

Azure stores the trophies

And Power BI waves the checkered flag 🏁

Thanks for joining us on this ride through the world of F1 data & cloud tech 🚀

## 📬 Contact
Team F1-Pipeline
For collaborations or questions, reach out via GitHub or LinkedIn

yaml
Copy
Edit

---

Let me know if you want this turned into a `README.md` file or want a logo/banner at the top!



## 📁 Project Structure

```bash
f1-data-pipeline/
│
├── .github/workflows/          # GitHub Actions CI/CD pipeline
│   └── data-pipeline.yml
├── data/
│   ├── raw/                    # Raw Kaggle dataset (CSV)
│   └── processed/              # Transformed & cleaned dataset
├── scripts/
│   └── transform.py            # Python script using pandas
├── README.md

