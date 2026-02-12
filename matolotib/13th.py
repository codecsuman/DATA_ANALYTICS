import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
data = pd.read_excel(
    "C:/Users/SUMAN JHANP/PROGRAMMING/DATA_ANALYTICS/ALL_xl/Food.xlsx"
)

df = pd.DataFrame(data)

# Group by Category
grouped = df.groupby("Category")[["Protein (g)", "Fat (g)"]].mean()

print(grouped)

# X-axis (numeric)
x = range(len(grouped))

# Stack plot
plt.stackplot(
    x,
    grouped["Protein (g)"],
    grouped["Fat (g)"],
    labels=["Protein", "Fat"]
)

plt.xticks(x, grouped.index, rotation=45)
plt.xlabel("Category")
plt.ylabel("Grams")
plt.title("Average Protein & Fat by Food Category")
plt.legend(loc="upper left")

plt.show()
