import pandas as pd


data = pd.read_excel ("ESD.xlsx")
print(data.head(10))
 
gp = data.groupby("Department").agg({"Gender":"cort"})
print(gp)