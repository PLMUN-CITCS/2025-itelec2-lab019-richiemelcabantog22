def get_student_score():
    student_score = float(input("Enter your score: "))
    return student_score

def calculate_grade(student_score):
    if student_score >= 90:
        return 'A'
    if student_score >= 80:
        return 'B'
    if student_score >= 70:
        return 'C'
    if student_score >= 60:
        return 'D'
    return 'F'

student_score = get_student_score()
grade = calculate_grade(student_score)
print(f"Your Grade is: {grade}")