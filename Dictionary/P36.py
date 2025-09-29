# 36.	Create a nested dictionary of students, where each student has name, age, and marks.
# Answer:
# Build nested dict keyed by roll or id.

n = int(input("How many students to enter? "))
students = {}
for i in range(n):
    sid = input(f"Student id for entry {i+1}: ")
    name = input("  Name: ")
    age = int(input("  Age: "))
    marks = float(input("  Marks: "))
    students[sid] = {"name": name, "age": age, "marks": marks}
print("Students nested dict:", students)
