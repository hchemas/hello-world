# Tuples. Tuples are immutable
import os
os.system("cls")
programming_languages = ("Python", "Java", "C#", "JavaScript", "Ruby", "Swift")
print(len(programming_languages))  # Length of the tuple
for i in range(len(programming_languages)):
    print(programming_languages[i])

#print first 3 elements
print(programming_languages[0:3])
# print las 3 elements
print(programming_languages[len(programming_languages)-3:])

vlanguage = input("Enter a programming language to know its position: ")
if vlanguage in programming_languages:
    position = programming_languages.index(vlanguage)
    print(vlanguage, "is at position", position)
else:
    print(vlanguage, "is not found in this tuple.")