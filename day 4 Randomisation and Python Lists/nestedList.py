fruits = ["strawberries", "apples", "grapes", "peaches", "pears"]
vegetables = ["spinach", "kale", "tomatoes", "celery", "potatoes"]

# nested list
dirty_dozen = [fruits, vegetables]

print(dirty-dozen)





# another example
fruits = ["strawberries", "apples", "grapes", "peaches", "pears"]
vegetables = ["spinach", "kale", "tomatoes", "celery", "potatoes"]

# nested list
dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)

# how it works: print(dirty_dozen[0]) will print fruits list
# print(dirty_dozen[1]) will print vegetables list
# print(dirty_dozen[1][1]) will print "kale"
# print(dirty_dozen[0][1]) will print "apples"
# the first index will determine which list to read from, 0 is fruits, 1 is vegetables
# the next index will determine which items to read from the nested list.

print(dirty_dozen[0][1])
print(dirty_dozen[1][1])