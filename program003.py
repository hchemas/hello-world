# strings, positions and slicing
import os
os.system("cls")
my_goal = "Learn Python!"
print(my_goal)
print(len(my_goal)) # length of the string
print(my_goal[0].upper())# first character and next characters in uppercase
print(my_goal[1].upper())
print(my_goal[2].upper())
print(my_goal[3].upper())
print(my_goal[4].upper())
print(my_goal[len(my_goal)-1].upper()) # last character in uppercase
# Negative index gives us the last character ina string
print(my_goal[-1].upper()) # last character in uppercase
# slice strings
print(my_goal[0:5],my_goal[6:len(my_goal)])
print(my_goal[:5])
print(my_goal[6:])
print(my_goal[6:12])
print(my_goal[6:len(my_goal)])


