import pandas as pd
import numpy as np

def audit_data(df):
    print("Rows:", len(df), "Cols:", len(df.columns))
    print("Missing:\n", df.isnull().sum())
    print("Duplicates:", df.duplicated().sum())

def clean_dataset(df, strategy="mean"):
    df = df.drop_duplicates()
    
    # Fill numeric missing values
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        val = df[col].mean() if strategy == "mean" else df[col].median()
        df[col] = df[col].fillna(val)
        
        # Clip outliers
        q1, q3 = df[col].quantile(0.25), df[col].quantile(0.75)
        iqr = q3 - q1
        df[col] = np.clip(df[col], q1 - 1.5 * iqr, q3 + 1.5 * iqr)
        
    return df
