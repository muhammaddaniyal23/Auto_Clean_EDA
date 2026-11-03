import pandas as pd
import numpy as np

def audit_data(df):
    """Prints a quick health check of the dataset."""
    print("\n--- DATA HEALTH AUDIT ---")
    print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
    print("\nMissing Values per Column:")
    print(df.isnull().sum()[df.isnull().sum() > 0])
    print(f"Duplicated Rows: {df.duplicated().sum()}")
    print("-------------------------\n")

def clean_dataset(df, fill_strategy="mean", handle_outliers=True):
    """Cleans missing data, removes duplicates, and handles outliers.""
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"-> Dropped {initial_rows - len(df)} duplicate rows.")
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        if df[col].isnull().sum() > 0:
            if fill_strategy == "mean":
                fill_val = df[col].mean()
            elif fill_strategy == "median":
                fill_val = df[col].median()
            else:
                fill_val = 0
            df[col] = df[col].fillna(fill_val)
            print(f"-> Imputed missing values in '{col}' with {fill_strategy}: {fill_val:.2f}")
    cat_cols = df.select_dtypes(include=[object, 'category']).columns
    for col in cat_cols:
        if df[col].isnull().sum() > 0:
            fill_val = df[col].mode()[0] if not df[col].mode().empty else "Unknown"
            df[col] = df[col].fillna(fill_val)
            print(f"-> Imputed missing values in categorical column '{col}' with mode: {fill_val}")
    if handle_outliers:
        for col in num_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df[col] = np.clip(df[col], lower_bound, upper_bound)
        print("-> Applied IQR outlier clipping to numerical features.")

    return df