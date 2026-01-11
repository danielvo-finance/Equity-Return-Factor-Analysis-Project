"""
Note:
- The sole purpose of this script is for the user to input the asset ticker(s) that they desire to analyze.
- Once the ticker is inputted, the data will be downloaded as a csv in data/raw/.
- The data should NOT be modified once downloaded.
"""

import yfinance as yf
import os

RAW_DIR = "data/raw"
ticker = input("Enter stock ticker(s) to analyze: ").upper()
start = input("Enter the start date of the data that you want (e.g. 2015-01-01): ")
end = input("Enter the end date of the data: ")

def download_data():
    df = yf.download(ticker, start, end, progress=False, auto_adjust=True)
    print(df)



for t in ticker:
    download_data()