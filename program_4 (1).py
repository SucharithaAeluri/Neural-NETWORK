class_score = float(input("Enter the class score: "))
if class_score >= 90:
    grade = 'A'
elif class_score >= 80:
    grade = 'B'
elif class_score >= 70:
    grade = 'C'
elif class_score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade:", grade)