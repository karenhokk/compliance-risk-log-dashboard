# Compliance Risk Log Dashboard | Python Compliance Analytics
Python script to process compliance risk event logs, generate summary reports and visual dashboard outputs for compliance review meetings.

## 🛡️ Data Privacy & PII Protection
1. Dummy anonymized dataset only committed to GitHub; real risk records with staff / third-party PII must remain local and secured.
2. All personal identifiers are removed or masked in the source data before analysis.
3. No raw confidential risk evidence / sensitive notes saved in outputs shared to GitHub.
4. Audit output files are not committed; `.gitignore` blocks production risk logs.
5. Report output can be saved locally only for internal compliance review.

## Project Objective
Automate aggregation of compliance risk incidents, calculate risk rating distribution, count open vs closed cases and export visual summary for compliance reporting.

## Features
- Load risk log CSV
- Categorize risks by risk level: High / Medium / Low
- Count open/closed incidents
- Generate simple matplotlib charts
- Export summary report CSV

## Tech Stack
Python, pandas, matplotlib

## How to Run
1. Clone repository
2. Install dependencies:
```bash
pip install pandas matplotlib
```
3. Run dashboard pipeline:
```bash
python risk_dashboard.py
```
