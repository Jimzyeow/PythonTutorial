#small pizza: $15 
# medium pizza: $20 
# large pizza: $25 
# pepperoni for small: +$2 
# for medium or large: +$3 
# extra cheese for any: + $1 

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
smallPizzaPrice = 15
mediumPizzaPrice = 20
largePizzaPrice = 25

if (size == 'S'):
    print(f"You have chosen small pizza, the price is {smallPizzaPrice}")
    bill += smallPizzaPrice

    if (add_pepperoni == 'Y'):
        bill += 2

elif (size == 'M'):
    print(f"You have chosen medium pizza, the price is ${mediumPizzaPrice}")
    bill += mediumPizzaPrice

    if (add_pepperoni == 'Y'):
        bill += 3

else:
    print(f"You have chosen large pizza, the price is ${largePizzaPrice}")
    bill += largePizzaPrice

    if (add_pepperoni == 'Y'):
        bill += 3

if (extra_cheese == 'Y'):
    bill += 1

print(f"Your final bill is: ${bill}")
