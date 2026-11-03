# AutoClean-EDA

A simple command-line tool for automating data cleaning and exploratory data analysis (EDA) using Python. I built this to speed up the repetitive parts of data preprocessing.

## What it does
Data Audit: Checks shape, missing values, duplicates, and column data types.
Cleaning: Drops duplicates, handles missing values (mean, median, or zero/mode imputation), and applies IQR clipping to manage outliers without losing rows.
EDA and Visuals: Automatically generates summary statistics and saves correlation heatmaps and distribution plots.

## Project Structure
- `cleaner.py` - Core data auditing and cleaning logic
- `eda.py` - Automated plotting and summary stats generator
- `eda_main.py` - CLI interface tying everything together

## How to use
Run it from your terminal like this:

```bash
python eda_main.py --input path/to/your_data.csv --strategy mean