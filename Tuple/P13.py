# 13.	Given a tuple ("Alice", 25, "Engineer"), unpack and print values with labels like Name: Alice.
# Answer:
# I unpack directly into variables.

t = eval(input("Enter a tuple like ('Alice', 25, 'Engineer'): "))
name, age, job = t
print("Name:", name)
print("Age:", age)
print("Profession:", job)
