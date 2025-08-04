import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("fahmidachowdhury/e-commerce-sales-analysis")
print("Path to dataset files:", path)

# Explore what files we have
print("\nFiles in dataset:")
for file in os.listdir(path):
    print(f"- {file}")
    
# Load and preview each CSV file
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]

for csv_file in csv_files:
    print(f"\n=== {csv_file} ===")
    df = pd.read_csv(os.path.join(path, csv_file))
    print(f"Shape: {df.shape}")
    print("Columns:", df.columns.tolist())
    print("\nFirst few rows:")
    print(df.head())
    print("\n" + "="*50)