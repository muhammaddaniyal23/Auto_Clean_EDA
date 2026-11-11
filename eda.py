import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_eda_reports(df, output_dir="output"):
    """Generates and saves automated EDA plots and summary statistics."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"\n-> Generating EDA reports in '{output_dir}/' folder...")
    summary = df.describe()
    summary.to_csv(os.path.join(output_dir, "summary_statistics.csv"))
    print("   Saved summary_statistics.csv")
    num_df = df.select_dtypes(include=['number'])
    if not num_df.empty and num_df.shape[1] > 1:
        plt.figure(figsize=(8, 6))
        sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
        plt.close()
        print("   Saved correlation_heatmap.png")
    for col in num_df.columns:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f"Distribution - {col}")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f"dist_{col}.png"))
        plt.close()
    print(f"   Saved distribution plots for {len(num_df.columns)} numerical columns.")