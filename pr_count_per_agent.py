import pandas as pd

df = pd.read_csv("aidev_sample.csv")

pr_counts = df["agent"].value_counts()
print("PR count per agent:")
print(pr_counts)
