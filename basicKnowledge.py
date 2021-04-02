#to print out the character in the string from the index position     
print("Hello"[4]) 

#Integer, python does not need to declare the data type unlike java
print(123+456)

#for large integer, instead of putting commas in between, can put underscore for better visualization
print(123_456_789)


#Float: decimal numbers
3.14159

#Boolean: true or false, have to be capital T or F
True
False 

#this will print the data type, e.g. int, string, float, etc
#use type() function to investigate the data type working with
num_char = len(input("Enter your name: "))
# print(type(num_char)) #print int type

#casting
new_num_char = str(num_char) #cast String to int
print("Your name has " + new_num_char + " characters")

a = float(123)
print(a)


#arithmetic operations
3+5
7-4
3*2
3/2 #give floating point number
2**5 #exponential, 2^5

#hierarchy - highest to lowest
()
**
* /
+ -


#to round up the number
print(round(8/3))

#set the decimal point precision
print(round(8/3, 2)) #2 decimal places

#floor division, will result back int value without casting
print(8//3)


#f-String, instead of casting int, float or boolean with str() in print function
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# this is to calculate the char inside a string. For example 
name = "Jimmy"
name.count('m')

#if there are multiple quotations, can use backslash to ignore a symbol
# this will escapes the string and see it as text
# .lower() method will convert the user input to lower case no matter what
# check other methods
input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()