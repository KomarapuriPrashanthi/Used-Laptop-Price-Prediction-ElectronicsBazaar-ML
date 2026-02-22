import pandas as pd
import re

# Load data and prevent pandas from treating 'N/A' as NaN
df = pd.read_csv("raw_laptop_data.csv", keep_default_na=False)

# Drop rows that contain "N/A" in any column
df = df[~df.isin(["N/A"]).any(axis=1)]



# 1. Normalize Storage(GB): convert TB to GB
def convert_storage(val):
    if val == "N/A":
        return val
    match = re.search(r"(\d+(?:\.\d+)?)\s*(TB|GB)", str(val).upper())
    if match:
        size = float(match.group(1))
        unit = match.group(2)
        return int(size * 1024) if unit == "TB" else int(size)
    return val

df["Storage(GB)"] = df["Storage(GB)"].apply(convert_storage)

# 2. Clean RAM(GB): extract numeric value
def clean_ram(val):
    if val == "N/A":
        return val
    match = re.search(r"(\d+)", str(val))
    return int(match.group(1)) if match else val

df["RAM(GB)"] = df["RAM(GB)"].apply(clean_ram)

# 3. Clean Screen Size(inch): extract numeric value
def clean_screen(val):
    if val == "N/A":
        return val
    match = re.search(r"([\d.]+)", str(val))
    return float(match.group(1)) if match else val

df["Screen Size(inch)"] = df["Screen Size(inch)"].apply(clean_screen)

# 4. Drop duplicate rows
df.drop_duplicates(inplace=True)

# 5. Save cleaned data to new CSV
df.to_csv("cleaned_laptop_data.csv", index=False)

print("✅ Cleaned data saved to 'cleaned_laptop_data.csv'")
