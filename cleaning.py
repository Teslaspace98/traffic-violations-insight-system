import pandas as pd
import numpy as np

print("Starting cleaning...")

# Load large CSV
df = pd.read_csv("traffic_violations_raw.csv", low_memory=False)

# Remove duplicate rows
df = df.drop_duplicates()

# Fix Date and Time
df["Date Of Stop"] = pd.to_datetime(df["Date Of Stop"], errors="coerce")
df["Time Of Stop"] = df["Time Of Stop"].astype(str).str.replace(".", ":", regex=False)

# Combine date and time
df["Stop_Timestamp"] = pd.to_datetime(
    df["Date Of Stop"].astype(str) + " " + df["Time Of Stop"],
    errors="coerce"
)

# Convert Yes/No type columns
bool_map = {
    "YES": True, "Y": True, "TRUE": True,
    "NO": False, "N": False, "FALSE": False
}

for col in df.columns:
    if df[col].dtype == object:
        df[col] = df[col].astype(str).str.upper().replace(bool_map)

# Fix latitude & longitude
if "Latitude" in df.columns:
    df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
if "Longitude" in df.columns:
    df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")

# Save cleaned file
df.to_csv("traffic_violations_cleaned.csv", index=False)

print("CLEANING DONE SUCCESSFULLY")
