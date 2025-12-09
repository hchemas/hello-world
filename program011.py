#Dictionaries
import os
os.system("cls")
stock_tickers = {"AAPL": "Apple Inc.","MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc.","AMZN": "Amazon.com Inc.","TSLA": "Tesla Inc.",
    "NVDA": "NVIDIA Corporation","META": "Meta Platforms Inc.","NFLX": "Netflix Inc."}

print(stock_tickers["MSFT"])

stock_tickers["DUSA"] = "Davis Fundamentals ETF" # add new key-value pair
stock_tickers["KLAR"] = "Klarna Group" # add new key-value pair
print(stock_tickers)

print(len(stock_tickers)) # length of dictionary

for i in range(len(stock_tickers)):
    key = list(stock_tickers.keys())[i]
    value = stock_tickers[key]
    print(key, ":", value)

search_ticker = input("Enter a stock ticker to find its company name: ")
if search_ticker in stock_tickers:
    print(search_ticker, "is", stock_tickers[search_ticker])

else:
    print(search_ticker, "is not in this dictionary.")

del_ticker = input("Enter a stock ticker to delete from the dictionary: ")
del_ticker = del_ticker.upper()
if del_ticker in stock_tickers:
    del stock_tickers[del_ticker]
    print(del_ticker, "has been deleted.")
    print(stock_tickers)
else:
    print(del_ticker, "is not in the dictionary.")

add_ticker = input("Enter a stock ticker to add to the dictionary: ")
add_ticker
add_company = input("Enter the company name for " + add_ticker + ": ")
stock_tickers[add_ticker] = add_company
print(stock_tickers)
