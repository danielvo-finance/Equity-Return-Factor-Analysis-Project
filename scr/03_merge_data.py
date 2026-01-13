"""
Notes:
- This script is to merge our processed data into a single DataFrame.
- This gives us a return matrix that is aligned by date and each column represents an asset.
"""

import pandas as pd
import os

DATA = "data/processed"

dfs = []

file = [f for f in os.listdir(DATA) if f.endswith("processed.csv")]
for f in file:
    ticker = f.split("_")[0]
    df = pd.read_csv(os.path.join(DATA, f))
    df["Date"] = pd.to_datetime(df["Date"])

    df = df[["Date", "Return"]].rename(columns={"Return": ticker})
    dfs.append(df)

combined_df = dfs[0]
for df in dfs[1:]:
    combined_df = pd.merge(combined_df, df, on="Date", how="outer")

combined_df.sort_values("Date", inplace=True)

combined_df.to_csv("data/combined_returns.csv", index=False)