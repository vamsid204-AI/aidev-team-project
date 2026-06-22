import pandas as pd

df = pd.read_csv("aidev_sample.csv")

print("Total rows:", len(df))
print("Columns:", list(df.columns))
print("Unique agents:", df["agent"].unique())
