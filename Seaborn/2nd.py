import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 

data = {"Days": [1,2,3,4,5,6,7],
         "NOP":[50,40,30,80,20,12,80]}
df = pd.DataFrame(data)
print(df)

sns.lineplot(data= data, x = "Days", y="NOP")
plt.show()