# Functions
import os
from datetime import datetime
os.system("cls")

def say_hi(name):
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        print("Good morning",name) 
    elif 12 <= current_hour < 17:
        print("Good afternoon",name)
    elif 17 <= current_hour < 21:
        print("Good evening",name)
    else:
        print("Good night",name)
    #print("Hi",name+"!")

name = ""
while name.upper() != "EXIT":
    name = input("Enter your name (or type 'EXIT' to quit): ")
    if name.upper() != "EXIT":
        say_hi(name)




