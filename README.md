# Crypto ETL Example (BTC, ETH, SOL)

## Data Source
This project uses historical cryptocurrency market data from **Yahoo Finance**, accessed via the `yfinance` Python library.  
The following trading pairs are downloaded:
- BTC-USD
- ETH-USD
- SOL-USD

Data is fetched at daily intervals for the most recent 30 days.

---

## How to Run the Project

1. Create and activate a Python virtual environment (optional but recommended)
2. Install dependencies:
   ```bash
   pip install pandas yfinance
3. Run the ETL script:
    ```bash
    python main.py
4. The processed dataset will be saved automatically.

---

## Output

The final cleaned dataset is saved to: 
    data/processed/output.csv


The output file contains:

- Date
- Daily closing prices for BTC, ETH, and SOL
- Daily percentage returns for each asset

All numeric values are rounded to two decimal places, rows are sorted by date, and incomplete rows are removed.