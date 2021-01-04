#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#this is a shorter way of calculating, for example the longer way of calculating would be:
# 0.12*150 = 18
#total bill including tips: 150+18 = 168; which is 112% of 150


#Format the result to 2 decimal places = 33.60


totalBill = input("What was the total bill? $")
tipPercentage = input("What percentage tip would you like to give? 10, 12, or 15?")
numberOfPeople = input("How many people to split the bill?")

totalTip = 1 + (int(tipPercentage)/100)
amountToPay = round((float(totalBill)/int(numberOfPeople)) * totalTip, 2)
print(f"Each person should pay: {amountToPay}")