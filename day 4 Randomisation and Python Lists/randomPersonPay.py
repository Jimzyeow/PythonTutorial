import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(names)
lengthList = len(names)
print(lengthList)
randomName = random.randint(0, lengthList - 1)
print(f"{names[randomName]} is going to buy the meal today!")
