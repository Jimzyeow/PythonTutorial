# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 
# It will take your current age as the input and output a message with our time left in this format:
# > You have x days, y weeks, and z months left. 
# Where x, y and z are replaced with the actual calculated numbers. 


age = input("What is your current age?")

finalAge = 90
final_months = finalAge*12
final_weeks = finalAge*52
final_days = finalAge*365

#remember to cast int as variable age returns String
userAge_months = int(age)*12
userAge_weeks = int(age)*52
userAge_days = int(age)*365

userMonths_left = final_months - userAge_months
userWeeks_left = final_weeks - userAge_weeks
userDays_left = final_days - userAge_days

# print(age)
# print(type(final_months))
# print(type(userAge_months))

print(f"You have {userDays_left} days, {userWeeks_left} weeks, and {userMonths_left} months left")



#another shorter way to do it
# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_reamining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12