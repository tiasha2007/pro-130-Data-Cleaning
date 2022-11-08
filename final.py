import pandas as pd
df=pd.read.csv("final.csv")

del df["Star_name"]
df=df.dropna()
df.to_csv("data.csv")