import pandas as pd

data1 = {"Emp id":["e01","e02","e03"],
        "Names":["ram","sam","jodu"],
        "Age":[20,30,40]}

data2 = {"Emp id":["e01","e02","e03"],
        "Names":["ram","sam","jodu"],
        "salary":[200,300,400]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1)
print()

print(df2)

print(pd.merge (df1,df2, on ="Emp id"))