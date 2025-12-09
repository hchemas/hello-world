# Program to print a list of stocks and its elements
import os
os.system("cls")
stocks = ["TOST", "GOOGL", "MSFT", "AMZN", "TSLA", "NVDA", "NFLX", "FIX"]
print(stocks)
for stock in stocks:
    print(stock)    
for i in range(len(stocks)):
    print(stocks[i])
print("Total number of stocks:", len(stocks))
print("First three stocks:", stocks[0:3])
print("Last three stocks:", stocks[-3:])
stocks.append("PYPL") 
print("After adding PYPL:", stocks) 
stocks.sort()
print(stocks) 