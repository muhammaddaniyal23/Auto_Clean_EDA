import argparse
import pandas as pd
import os
from cleaner import audit_data, clean_dataset
from eda import generate_eda_reports

def main():
    parser = argparse.ArgumentParser(description="AutoClean-EDA: Automated Data Cleaning & EDA Tool")
    parser.add_argument("--input", required=True, help="Path to the raw input CSV file")
    parser.add_argument("--output", default="output/cleaned_data.csv", help="Path to save the cleaned CSV")
    parser.add_argument("--strategy", default="mean", choices=["mean", "median", "zero"], help="Imputation strategy for missing values")
    
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        return

    print(f"Loading dataset from {args.input}...")
    df = pd.read_csv(args.input)
    audit_data(df)
    generate_eda_reports(df)
    print("\nStarting data cleaning pipeline...")
    cleaned_df = clean_dataset(df, fill_strategy=args.strategy)
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    cleaned_df.to_csv(args.output, index=False)
    print(f"\nSuccess! Cleaned data saved to {args.output}")

if __name__ == "__main__":
    main()