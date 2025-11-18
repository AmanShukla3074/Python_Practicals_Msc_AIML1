# 9. Program to sort a list of dictionaries by a specific key using lambda.
students = [{"name": "A", "age": 22}, {"name": "B", "age": 20}]
sorted_students = sorted(students, key=lambda x: x["age"])
print(sorted_students)
