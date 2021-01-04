year = int(input("Which year do you want to check? "))


if(year%4 == 0):
	if(year%100 != 0):
		print(f"Year {year} is a Leap year")
	elif((year%100 == 0) and (year%400 == 0)):
		print(f"Year {year} is a Leap year")
	else:
		print(f"Year {year} is a Not a Leap year")
else:
	print(f"Year {year} is a Not a Leap year")
