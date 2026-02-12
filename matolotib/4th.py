import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Read Excel file
# -------------------------------
file_path = "C:/Users/SUMAN JHANP/PROGRAMMING/DATA_ANALYTICS/ALL_xl/20_people_data.xlsx"
df = pd.read_excel(file_path)

# -------------------------------
# 2. Clean column names
# -------------------------------
df.columns = df.columns.str.strip()

# -------------------------------
# 3. Print column names (debug)
# -------------------------------
print("Columns in file:", df.columns)

# -------------------------------
# 4. Find Date column safely
# -------------------------------
date_col = None
for col in df.columns:
    if col.lower() == "date":
        date_col = col
        break

if date_col is None:
    raise ValueError("❌ No Date column found in Excel file")

# -------------------------------
# 5. Convert Date column
# -------------------------------
df[date_col] = pd.to_datetime(df[date_col])

# -------------------------------
# 6. Line Plot
# -------------------------------
plt.plot(df[date_col], df["Amount"], marker="o")

plt.xlabel("Date")
plt.ylabel("Amount")
plt.title("Amount Trend Over Time")

plt.xticks(rotation=20)
plt.tight_layout()

plt.show()
