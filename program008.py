# Lists. Listas are mutable (can be changed)
import os
os.system("cls")
favorite_stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "NVDA", "MU"]
print(len(favorite_stocks)) # length of list
print(favorite_stocks)
for i in range(len(favorite_stocks)): # print all the elements in the list
    print(favorite_stocks[i])

# print first 3 elements
print(favorite_stocks[0:3])
# print first 3 elements independently
for i in range(3):
    print(favorite_stocks[i])

# replace values in the list
favorite_stocks[4] = "EZPW"
print(favorite_stocks)

# add values to the list
favorite_stocks.append("VRT")
print(favorite_stocks)

# insert value at specific position
favorite_stocks.insert(1,"KGC")
print(favorite_stocks)

# remove value from the list
favorite_stocks.remove("AMZN")
print(favorite_stocks)

# sort the list
favorite_stocks.sort()
print(favorite_stocks)

# remove all elements from the list
favorite_stocks.clear()
print(favorite_stocks)
