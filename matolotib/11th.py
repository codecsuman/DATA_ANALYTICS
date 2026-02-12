import pandas as pd 

data = pd.read_excel('')
df = pd.DataFrame(data)
df2 =(df.head(50))

plt.plot (df2["Age"])
plt.show()