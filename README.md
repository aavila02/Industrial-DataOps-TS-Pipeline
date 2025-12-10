# Industrial DataOps Pipeline

A Python-based data processing pipeline for IoT-Integrated Predictive Maintenance time-series data. This project provides tools for loading, exploring, and cleaning industrial sensor data to prepare it for analysis and machine learning applications.

## Overview

This pipeline processes IoT maintenance data collected from industrial equipment, performing essential data quality checks and transformations. The project is designed to handle time-series sensor data including temperature, vibration, acoustic, and current measurements.

## Features

- **Data Loading & Exploration**: Load and inspect IoT maintenance datasets with comprehensive statistics
- **Timestamp Integrity Validation**: Verify datetime formatting and detect missing timestamps
- **Temperature Range Validation**: Identify unrealistic temperature readings (e.g., below 0°C)
- **Outlier Detection**: Use Interquartile Range (IQR) method to detect anomalies in vibration data
- **Data Transformation**: Create cleaned datasets with standardized column names and selected features

## Requirements

- Python 3.8+
- pandas >= 2.0.0
- numpy >= 1.24.0

## Installation

1. Clone or download this repository

2. Create a virtual environment (recommended):
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
industrial-dataops-pipeline/
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── iot_maintenance_data.csv   # Input dataset
├── load_data.py              # Data loading and exploration script
└── clean_data.py             # Data cleaning and quality checks script
```

## Usage

### Phase 1: Data Loading and Exploration

Run the initial data loading script to explore the dataset:

```bash
python3 load_data.py
```

This script will:
- Load the IoT maintenance dataset
- Display dataset shape and structure
- Show first 5 rows
- Display column information and data types
- Provide descriptive statistics

### Phase 2: Data Cleaning and Quality Checks

Run the data cleaning script to perform quality checks and transformations:

```bash
python3 clean_data.py
```

This script performs:
1. **Timestamp Integrity Check**: Verifies datetime format and counts null values
2. **Temperature Range Check**: Identifies records with unrealistic temperatures (< 0°C)
3. **Vibration Outlier Detection**: Uses IQR method to detect outliers in vibration data
4. **Data Transformation**: Creates a cleaned dataset with:
   - `timestamp`: Time of measurement
   - `asset_id`: Machine/asset identifier (renamed from `machine_id`)
   - `temperature_c`: Temperature in Celsius (renamed from `temperature`)
5. **Output Display**: Shows the first 5 rows and data types of the transformed dataset

## Dataset Description

The `iot_maintenance_data.csv` file contains time-series sensor data with the following columns:

- **timestamp**: DateTime of the measurement
- **machine_id**: Identifier for the machine/asset
- **vibration**: Vibration sensor reading
- **acoustic**: Acoustic sensor reading
- **temperature**: Temperature reading in Celsius
- **current**: Electrical current measurement
- **IMF_1, IMF_2, IMF_3**: Intrinsic Mode Functions (signal decomposition features)
- **label**: Binary classification label (0 = normal, 1 = anomaly)

## Data Quality Checks

The cleaning script performs several quality checks:

1. **Timestamp Integrity**: Ensures all timestamps are valid datetime objects and identifies any missing values
2. **Temperature Validation**: Flags unrealistic temperature readings (below 0°C for industrial equipment)
3. **Outlier Detection**: Uses the IQR method to identify statistical outliers in vibration data:
   - Calculates Q1 (25th percentile) and Q3 (75th percentile)
   - Computes IQR = Q3 - Q1
   - Defines outliers as values outside [Q1 - 1.5×IQR, Q3 + 1.5×IQR]

## Output

The `clean_data.py` script produces a `transformed_data` DataFrame containing only the essential columns with standardized naming:
- `timestamp`: DateTime column
- `asset_id`: Machine identifier
- `temperature_c`: Temperature in Celsius

This cleaned dataset is ready for further analysis, feature engineering, or machine learning model training.

## License

This project is provided as-is for educational and development purposes.

## Contributing

Contributions, issues, and feature requests are welcome. Please feel free to submit a pull request or open an issue.

