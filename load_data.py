"""
Industrial DataOps - Time-Series Data Processing
Initial Data Loading and Exploration Script

This script loads the IoT-Integrated Predictive Maintenance Dataset
and displays key information about the data structure and statistics.
"""

import pandas as pd
import numpy as np

# Load the CSV file
print("=" * 80)
print("Loading IoT Maintenance Data...")
print("=" * 80)
df = pd.read_csv('iot_maintenance_data.csv', parse_dates=['timestamp'])

# Display basic information about the dataset
print(f"\nDataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\n{'=' * 80}")
print("FIRST 5 ROWS OF THE DATASET")
print("=" * 80)
print(df.head())

print(f"\n{'=' * 80}")
print("COLUMN NAMES AND DATA TYPES (df.info())")
print("=" * 80)
df.info()

print(f"\n{'=' * 80}")
print("DESCRIPTIVE STATISTICS (df.describe())")
print("=" * 80)
print(df.describe())

print(f"\n{'=' * 80}")
print("DATA LOADING COMPLETE - Ready for Data Cleaning Phase")
print("=" * 80)

