import pandas as pd

df = pd.read_csv("aidev_sample.csv")

avg_size = df.groupby("agent")["lines_changed"].mean()
print("Average lines changed per PR, by agent:")
print(avg_size)

