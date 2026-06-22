import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("aidev_sample.csv")
df["created_at"] = pd.to_datetime(df["created_at"])

monthly = df.set_index("created_at").resample("ME").size()
monthly.plot(kind="line", title="PRs Submitted Over Time")
plt.xlabel("Month")
plt.ylabel("Number of PRs")
plt.savefig("pr_over_time.png")
print("Chart saved as pr_over_time.png")
