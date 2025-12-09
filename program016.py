# Functions
import os
os.system("cls")

def count_vowels(word):
    num_vowels = 0
    for char in word:
        if char.lower() in "aeiou":
            num_vowels += 1
    return(num_vowels)


word = ""
while word.upper() != "EXIT":
    word = input("Enter a word (or type 'EXIT' to quit): ")
    if word.upper() != "EXIT":
        print("The number of vowels in",word,"are:",count_vowels(word))
