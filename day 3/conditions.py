print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("Please enter")
  age = int(input("What is your age?"))

#python uses 'or' 'and' for if statement
  if(age < 12):
    print("Please pay $5")
  elif(age >= 12 and age <= 18):
    print("Please pay $7")
  else:
    print("Please pay $12")

else:
  print("You cannot enter")  