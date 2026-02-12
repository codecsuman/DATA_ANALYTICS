import pandas as pd

# Read Excel file
data = pd.read_excel("practice_1.xlsx")
print(data)

# Create Bonus column (20% of Salary)
data["Bonus"] = (data["Salary"] / 100) * 20
print(data)

# Create another DataFrame
data2 = {"Month": ["January", "February", "March", "April"]}

b = pd.DataFrame(data2)
print(b)
