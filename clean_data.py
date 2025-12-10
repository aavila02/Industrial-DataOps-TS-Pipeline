"""
Industrial DataOps - Time-Series Data Processing
Data Cleaning and Quality Checks Script

This script performs data quality checks including timestamp integrity,
temperature range validation, vibration outlier detection, and creates
a transformed dataset with selected and renamed columns.
"""

import pandas as pd
import numpy as np

# Load the CSV file
print("=" * 80)
print("Loading IoT Maintenance Data for Cleaning...")
print("=" * 80)
df = pd.read_csv('iot_maintenance_data.csv', parse_dates=['timestamp'])

print(f"\nDataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")

# ============================================================================
# 1. TIMESTAMP INTEGRITY CHECK
# ============================================================================
print(f"\n{'=' * 80}")
print("TIMESTAMP INTEGRITY CHECK")
print("=" * 80)

# Verify timestamp is datetime type
print(f"Timestamp column data type: {df['timestamp'].dtype}")

# Check for null values in timestamp column
null_timestamps = df['timestamp'].isna().sum()
print(f"Number of null values in timestamp column: {null_timestamps}")

# ============================================================================
# 2. TEMPERATURE RANGE CHECK
# ============================================================================
print(f"\n{'=' * 80}")
print("TEMPERATURE RANGE CHECK")
print("=" * 80)

# Identify rows where temperature is less than 0 degrees Celsius
invalid_temperature = df[df['temperature'] < 0]
invalid_temperature_count = len(invalid_temperature)
print(f"Number of records with temperature < 0°C: {invalid_temperature_count}")

# ============================================================================
# 3. VIBRATION OUTLIER DETECTION (IQR METHOD)
# ============================================================================
print(f"\n{'=' * 80}")
print("VIBRATION OUTLIER DETECTION (IQR METHOD)")
print("=" * 80)

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df['vibration'].quantile(0.25)
Q3 = df['vibration'].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Q1 (25th percentile): {Q1:.4f}")
print(f"Q3 (75th percentile): {Q3:.4f}")
print(f"IQR: {IQR:.4f}")
print(f"Lower bound (Q1 - 1.5×IQR): {lower_bound:.4f}")
print(f"Upper bound (Q3 + 1.5×IQR): {upper_bound:.4f}")

# Identify outliers
vibration_outliers = df[(df['vibration'] < lower_bound) | (df['vibration'] > upper_bound)]
outlier_count = len(vibration_outliers)
print(f"Total number of outliers in Vibration column: {outlier_count}")

# ============================================================================
# 4. DATA TRANSFORMATION
# ============================================================================
print(f"\n{'=' * 80}")
print("DATA TRANSFORMATION")
print("=" * 80)

# Create transformed_data DataFrame with selected columns
transformed_data = df[['timestamp', 'machine_id', 'temperature']].copy()

# Rename columns
transformed_data = transformed_data.rename(columns={
    'machine_id': 'asset_id',
    'temperature': 'temperature_c'
})

print("Created transformed_data DataFrame with columns: timestamp, asset_id, temperature_c")

# ============================================================================
# 5. OUTPUT DISPLAY
# ============================================================================
print(f"\n{'=' * 80}")
print("TRANSFORMED DATA - FIRST 5 ROWS")
print("=" * 80)
print(transformed_data.head())

print(f"\n{'=' * 80}")
print("TRANSFORMED DATA - DATA TYPES")
print("=" * 80)
print(transformed_data.dtypes)

print(f"\n{'=' * 80}")
print("DATA CLEANING COMPLETE")
print("=" * 80)

