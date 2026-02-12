import pandas as pd 

data = {
    "keys": ["k1", "k2", "k3", "k4"],
    "Names": ["john", "ben", "devid", "pater"],
    "Houses": ["red", "blue", "green", "red"]
}

df = pd.DataFrame(data)
print(df)

pivot_df = df.pivot(index="keys", columns="Names", values="Houses")
print(pivot_df)
