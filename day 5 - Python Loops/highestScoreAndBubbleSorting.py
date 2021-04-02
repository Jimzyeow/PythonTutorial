# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# range function is: range(start, stop, step)
# start and step is optional to key in a value. start default is 0, step default is 1
# start is which position to start, stop is which position to stop, step specify the incrementation.

# example input 78 65 89 86 55 91 64 89

# print(len(student_scores))
highestScore = 0

# score will store the index value, e.g. student_scores[1] = 78
for n in range(0, len(student_scores)):
    if student_scores[n] > highestScore:
        highestScore = student_scores[n]

print(f"The highest score is: {highestScore}\n")

# to sort the score in ascending order
numberOfScores = len(student_scores) #if 8
temp = 0

for i in range(0, numberOfScores-1): # 8-1 = 7, last index in list of 8 items
    # comparing up to 6 (starting from first index where  i = 0: 8 - 0 - 1 = 7)
    # have to -1, if i = 0, numberOfScores = 8, 8 - 0 = 8, student_scores[8] will be out of bounds
    for j in range(0, numberOfScores-i-1):
        if student_scores[j] > student_scores[j+1]:
            temp = student_scores[j+1]
            student_scores[j + 1] = student_scores[j]
            student_scores[j] = temp

print(f"Ascending order: {student_scores}")


# to sort the score in descending order
numberOfScores = len(student_scores) #if 8
temp = 0

for i in range(0, numberOfScores-1): # 8-1 = 7, last index in list of 8 items
    # comparing up to 6 (starting from first index where  i = 0: 8 - 0 - 1 = 7)
    # have to -1, if i = 0, numberOfScores = 8, 8 - 0 = 8, student_scores[8] will be out of bounds
    for j in range(0, numberOfScores-i-1):
        if student_scores[j] < student_scores[j+1]:
            temp = student_scores[j]
            student_scores[j] = student_scores[j+1]
            student_scores[j+1] = temp

print(f"Descending order: {student_scores}")
