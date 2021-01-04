print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
userInput = input("Would you like to go left or right? ").lower()

if(userInput == "left"):
  print("You came across a lake, the waves are calm but something doesn't feel right")
  userInput = input("Would you like to swim or wait? ").lower()
  if(userInput == "wait"):
    print("You waited and you saw a donkey, you decided to follow the donkey hoping to lead you to a safe point")
    print("You come across 3 doors: Red, Blue, and Yellow")
    userInput = input("Which one will you choose? Red, blue or yellow? ").lower()
    if(userInput == "red"):
      print("A sudden fire burst into your face as you open the red door.\nGame over")
    elif(userInput == "blue"):
      print("A giant beast suddenly appear in front of you and devour you.\nGame over")
    else:
      print("You win the game!")
  else:
    print("You are attack by a shark.\nGame over")
else:
  print("You fall into a hole.\nGame over")