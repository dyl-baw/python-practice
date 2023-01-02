#Get user input for the student scores
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

#Find the highest score in this list given to us by the user.
highest_score = student_scores[0]
for x in range(0, len(student_scores)):
    if(highest_score < student_scores[x]):
        highest_score = student_scores[x]
print(f"The highest score in the class is: {highest_score}")