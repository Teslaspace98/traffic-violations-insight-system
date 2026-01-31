import matplotlib
matplotlib.use("TkAgg")

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("traffic_violations_cleaned.csv")

print("Total records:", len(df))

# Top 10 violation types
df["Violation Type"].value_counts().head(10).plot(
    kind="bar", title="Top 10 Violation Types"
)
plt.show()

# Violations by hour
df["Stop_Timestamp"] = pd.to_datetime(df["Stop_Timestamp"])
df["Hour"] = df["Stop_Timestamp"].dt.hour
df["Hour"].value_counts().sort_index().plot(
    title="Violations by Hour"
)
plt.show()

# Gender distribution
df["Gender"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", title="Gender Distribution"
)
plt.show()
