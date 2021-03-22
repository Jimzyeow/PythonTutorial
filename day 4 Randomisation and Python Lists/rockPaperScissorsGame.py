import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
user_choice = input("What is your choice? \n"
                    "1. Rock\n"
                    "2. Paper\n"
                    "3. Scissors\n")

computer_choice = random.randint(1, 3)

# print(len(game)) //output 3
# print(type(int(user_choice))) //output int

if int(user_choice) > len(game):
    print("Please enter a value above")
elif int(user_choice) < 1:
    print("Please enter proper value")
else:
    print(f"You chose : {game[int(user_choice)-1]}")
    print(f"The computer chose: {game[int(computer_choice)-1]}")

# if int(user_choice)-1 == 0 and int(computer_choice)-1 == 0:
#     print("It is a draw!")
if int(user_choice)-1 == 0 and int(computer_choice)-1 == 1:
    print("Computer wins")
elif int(user_choice)-1 == 0 and int(computer_choice)-1 == 2:
    print("You win!")
elif int(user_choice)-1 == 1 and int(computer_choice)-1 == 0:
    print("You win!")
elif int(user_choice)-1 == 1 and int(computer_choice)-1 == 2:
    print("Computer wins")
elif int(user_choice)-1 == 2 and int(computer_choice)-1 == 0:
    print("Computer wins")
elif int(user_choice)-1 == 2 and int(computer_choice)-1 == 1:
    print("You win!")
else:
    print("It is a draw")