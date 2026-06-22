import pandas as pd

df = pd.read_csv("aidev_sample.csv")

merge_rate = df.groupby("agent")["merged"].mean() * 100
print("Merge rate per agent (%):")
print(merge_rate)

