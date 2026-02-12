import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Read Excel file
# -------------------------------
file_path = "C:/Users/SUMAN JHANP/PROGRAMMING/DATA_ANALYTICS/ALL_xl/20_people_data.xlsx"
df = pd.read_excel(file_path)

# -------------------------------
# 2. Clean column names (IMPORTANT)
# -------------------------------
df.columns = df.columns.str.strip()

# -------------------------------
# 3. Print data & columns (debug)
# -------------------------------
print(df)
print(df.columns)

# -------------------------------
# 4. Group data (to avoid overlap)
# -------------------------------
grouped_data = df.groupby("Payment Mode")["Amount"].sum()

# -------------------------------
# 5. Bar Chart
# -------------------------------
plt.bar(grouped_data.index, grouped_data.values)
plt.xlabel("Payment Mode")
plt.ylabel("Total Amount")
plt.title("Total Amount by Payment Mode")

# -------------------------------
# 6. Show plot
# -------------------------------
plt.show()
