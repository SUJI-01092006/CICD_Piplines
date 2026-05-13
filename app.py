def calculate_grade(mark):
    if mark >= 90:
        return "A Grade"
    elif mark >= 75:
        return "B Grade"
    elif mark >= 50:
        return "C Grade"
    else:
        return "Fail"

student_name = "Suji"
mark = 87

grade = calculate_grade(mark)

print("===== Student Grade Report =====")
print("Student Name :", student_name)
print("Student Mark :", mark)
print("Student Grade:", grade)
print("CI Pipeline Build Successful")
