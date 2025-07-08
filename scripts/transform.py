import pandas as pd
import os

# Define input and output paths
input_path = "data/raw/driver_value.csv"
output_path = "data/processed/driver_value_cleaned.csv"

# Read raw data
df = pd.read_csv(input_path)

# Display the first few rows
print("Original Data:")
print(df.head())

# Drop rows with any missing values
df_cleaned = df.dropna()

# Normalize column names
df_cleaned.columns = [col.strip().lower().replace(" ", "_") for col in df_cleaned.columns]

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Save cleaned data
df_cleaned.to_csv(output_path, index=False)

print(f"\n✅ Processed data saved to: {output_path}")
