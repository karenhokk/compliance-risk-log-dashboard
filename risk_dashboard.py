import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    df = pd.read_csv("sample_risk_log.csv")
    print("=== Compliance Risk Summary ===")
    print(df["risk_level"].value_counts())
    print(df["status"].value_counts())

    # Ensure local output directory exists for the script
    os.makedirs("output", exist_ok=True)

    # Chart
    risk_counts = df["risk_level"].value_counts()
    risk_counts.plot(kind="bar", color=["red", "orange", "green"])
    plt.title("Risk Level Distribution")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("output/risk_summary.png")
    plt.close()

    summary = df.groupby(["risk_level","status"]).size().reset_index(name="count")
    summary.to_csv("output/risk_summary_report.csv", index=False)
    print("Report saved to output folder")

if __name__ == "__main__":
    main()
