import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_eda_reports(df, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    
    print("\n-Summary Stats")
    print(df.describe())
    
    num_df = df.select_dtypes(include=["number"])
    if not num_df.empty and num_df.shape[1] > 1:
        plt.figure(figsize=(8, 6))
        sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
        plt.close()
    for col in num_df.columns[:5]:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f"Distribution - {col}")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f"dist_{col}.png"))
        plt.close()
        
    print(f"EDA charts saved to '{output_dir}/'")
