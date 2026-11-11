import argparse
import pandas as pd
import os
from cleaner import audit_data, clean_dataset
from eda import generate_eda_reports

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", default="output/cleaned.csv")
    parser.add_argument("-s", "--strategy", default="mean")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"File not found: {args.input}")
        return

    df = pd.read_csv(args.input)
    audit_data(df)
    generate_eda_reports(df)
    
    cleaned_df = clean_dataset(df, fill_strategy=args.strategy)
    
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    cleaned_df.to_csv(args.output, index=False)
    print("Done. Saved to", args.output)

if __name__ == "__main__":
    main()
