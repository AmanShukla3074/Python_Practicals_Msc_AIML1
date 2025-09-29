# 1.	Create a dictionary to store a student’s details (name, age, grade). Print the grade.
# Answer:
# I create a dictionary from user input and print the 'grade' field.

name = input("Student name: ")
age = input("Student age: ")
grade = input("Student grade: ")
student = {"name": name, "age": age, "grade": grade}
print("Student grade is:", student["grade"])
