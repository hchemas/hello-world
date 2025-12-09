import os
os.system("cls")
# Help me asking the number of stocks I want to add to a list and then printing the list and each stock in a separate line
stocks = []
num_stocks = int(input("How many stocks do you want to add? "))
for i in range(num_stocks):
    stock = input("Enter stock symbol #{}: ".format(i + 1))
    stocks.append(stock)
stocks.sort()
print("Stocks list:", stocks)
for stock in stocks:
    print(stock)
# Now I want to be able to enter a Stock ticker and find its position in the list
search_stock = input("Enter a stock symbol to find its position: ")
if search_stock in stocks:
    position = stocks.index(search_stock) + 1  # +1 to convert from 0-based to 1-based index
    print("{} is at position {}".format(search_stock, position))
else:
    print("{} is not in the list.".format(search_stock))