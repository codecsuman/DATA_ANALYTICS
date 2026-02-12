import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_excel ("C:/Users/SUMAN JHANP/PROGRAMMING/DATA_ANALYTICS/ALL_xl/20_people_data.xlsx")
df= pd.DataFrame(data)
grouped_by= df.groupby("Payment Mode")["Amount"].sum()
print(grouped_by)
plt.pie(grouped_by.values,labels=grouped_by.index,autopct="%.2f")
plt.show()
print(df)