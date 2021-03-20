import random
# import my_module

#randint(a,b) will return random number where a <= number <= b
random_integer = random.randint(1,20)
print(random_integer)

#print random float number between 0.0 to 1.0
random_float = random.random()
print(random_float)

#if wants number from 0.00000... - 4.99999999
print(random_float * 5)

# print(my_module.pi)