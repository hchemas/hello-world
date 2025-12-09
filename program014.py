# While Loop to Collect Favorite Stock Symbols
import os
os.system("cls")
favorite_stocks = []
stock = ""
while stock.upper() != "EXIT":
    stock = input("Enter a stock symbol to add to your favorites (or type 'EXIT' to finish): ")
    if stock.upper() != "EXIT":
        favorite_stocks.append(stock)

print("You have entered a total of", len(favorite_stocks), "stocks.")
favorite_stocks.sort()
print("Your favorite stocks in alphabetical order are:")
for i in range(len(favorite_stocks)):
    print(favorite_stocks[i])
