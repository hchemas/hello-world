# Lists and Input
import os
os.system("cls")
favorite_stocks = []
num_stocks = int(input("How many stocks do you want to enter? "))
if num_stocks <= 0:
    print("You must enter at least one stock.")
    exit()
for i in range(num_stocks):
    stock = input("Enter stock symbol #" + str(i+1) + ": ")
    favorite_stocks.append(stock)

print("You have entered a total of", len(favorite_stocks), "stocks.")

print("Your favorite stocks are:")
for i in range(len(favorite_stocks)):
    print(favorite_stocks[i])

print("Your favorite stocks in alphabetical order are:")
favorite_stocks.sort()
for i in range(len(favorite_stocks)):
    print(favorite_stocks[i])

# how do I find the position of a value in the list?
search_stock = input("Enter a stock symbol to find its position: ")
if search_stock in favorite_stocks:
    position = favorite_stocks.index(search_stock)
    print(search_stock, "is at position", position)
else:   
    print(search_stock, "is not in your favorite stocks list.")
    


