# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
# not using the len() and sum() function
# Example Input
# ``
# 156 178 165 171 187
# ```

print(f"The list of student height is: {student_heights}")
print(type(student_heights[1]))

totalHeight = 0
totalStudents = 0 # act as counter in for loop

for height in student_heights:
  print(height)
  totalHeight += height
  totalStudents += 1

averageHeight = totalHeight / totalStudents

print(f"The total height is {int(totalHeight)} for {len(student_heights)} students \n"
      f"and the average height is {round(averageHeight)}")
