#Dictionaries
import os
os.system("cls")
stock_tickers = {"AAPL": "Apple Inc.","MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc.","AMZN": "Amazon.com Inc.","TSLA": "Tesla Inc.",
    "NVDA": "NVIDIA Corporation","META": "Meta Platforms Inc.","NFLX": "Netflix Inc."}

for ticker,company_name in stock_tickers.items():
    print(ticker, ":", company_name)

