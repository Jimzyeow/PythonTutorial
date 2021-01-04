#true love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

totalScore1 = 0
totalScore2 = 0
name1 = name1.lower()
name2 = name2.lower()

#TRUE
tOccurence = name1.count('t')
tOccurence2 = name2.count('t')
totalTOccurence = tOccurence + tOccurence2
print(f"T occurs {totalTOccurence} times")

rOccurence = name1.count('r')
rOccurence2 = name2.count('r')
totalROccurence = rOccurence + rOccurence2
print(f"R occurs {totalROccurence} times")

uOccurence = name1.count('u')
uOccurence2 = name2.count('u')
totalUOccurence = uOccurence + uOccurence2
print(f"U occurs {totalUOccurence} times")

eOccurence = name1.count('e')
eOccurence2 = name2.count('e')
totalEOccurence = eOccurence + eOccurence2
print(f"E occurs {totalEOccurence} times")

totalScore1 += totalTOccurence + totalROccurence + totalUOccurence + totalEOccurence
print(f"Total: {totalScore1}")

#LOVE
LAppear = name1.count('l')
LAppear2 = name2.count('l')
totalLAppear = LAppear + LAppear2
print(f"L occurs {totalLAppear} times")

OAppear = name1.count('o')
OAppear2 = name2.count('o')
totalOAppear = OAppear + OAppear2
print(f"O occurs {totalOAppear} times")

VAppear = name1.count('v')
VAppear2 = name2.count('v')
totalVAppear = VAppear + VAppear2
print(f"V occurs {totalVAppear} times")

EAppear = name1.count('e')
EAppear2 = name2.count('e')
totalEAppear = EAppear + EAppear2
print(f"E occurs {totalEAppear} times")

totalScore2 += totalLAppear + totalOAppear + totalVAppear + totalEAppear
print(f"Total: {totalScore2}")

# loveScore = (totalScore1 * 10) + totalScore2
#another way is to do casting
loveScore = int(str(totalScore1) + str(totalScore2))
print(f"Your score is {loveScore}")

if (loveScore < 10 or loveScore > 90):
  print(f"Your score is {loveScore}, you go together like coke and mentos")

elif (loveScore > 40 and loveScore < 50):
  print(f"Your score is {loveScore}, you are alright together")

else:
  print(f"Your score is {loveScore}")