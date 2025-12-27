# Extract → Transform → Load

import os
import pandas as pd
import yfinance as yf

# --- 1. Extract ---
print("🔹 Extracting data from Yahoo Finance...")

# Define the tickers for most popular crypto
tickers = ["BTC-USD", "ETH-USD", "SOL-USD"]

# Download recent data (last 30 days)
data = yf.download(tickers, period="30d", interval="1d")

# Display first few rows
print("✅ Data extracted!")
data.head()

# --- 2. Transform ---
print("🔹 Transforming data...")

# 1) Selecting columns: keep only Close prices
df = data["Close"].reset_index()

# 2) Renaming columns
df.columns = ["Date", "BTC", "ETH", "SOL"]

# 3) Filtering rows: keep only last 14 days
df = df.tail(14)

# 4) Computing new columns: daily returns (%)
df["BTC_return_%"] = df["BTC"].pct_change() * 100
df["ETH_return_%"] = df["ETH"].pct_change() * 100
df["SOL_return_%"] = df["SOL"].pct_change() * 100

# 5) Sorting values by Date (ascending)
df = df.sort_values("Date")

# 6) Rounding
df = df.round(2)

# Drop first row with NaN returns
df = df.dropna()

print("✅ Data transformed!")
df

# --- 3. Load ---
print("🔹 Saving transformed data to CSV...")

os.makedirs("../data/processed", exist_ok=True)
df.to_csv("../data/processed/output.csv", index=False)

print("✅ File saved to data/processed/output.csv")
