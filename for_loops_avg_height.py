#Quick script to calculate average of heights in cm.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

result = 0
for y in range(0, len(student_heights)):
    result += student_heights[y]

average = result / len(student_heights)
print(round(average))