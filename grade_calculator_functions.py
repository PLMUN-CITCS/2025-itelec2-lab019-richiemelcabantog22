def get_student_score():
   score = float(input("Enter your score: "))
   return score


def calculate_grade(score):
   if score >= 90:
       return 'A'
   elif score >= 80:
       return 'B'
   elif score >= 70:
       return 'C'
   elif score >= 60:
       return 'D'
   else:
       return 'F'


score = get_student_score() 
grade = calculate_grade(score) 
print(f"Your Grade is: {grade}")
