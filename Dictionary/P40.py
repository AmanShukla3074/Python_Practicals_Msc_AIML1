# 40.	Create a dictionary of classrooms, each having a list of students.
# Answer:
# Classroom names map to lists of student names.

n = int(input("How many classrooms? "))
classrooms = {}
for _ in range(n):
    cname = input("Class name: ")
    studs = input("Students (space separated): ").split()
    classrooms[cname] = studs
print("Classrooms:", classrooms)
