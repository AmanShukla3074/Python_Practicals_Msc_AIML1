# 12.	Swap two variables using tuple unpacking: a = 5, b = 10.
# Answer:
# Tuple unpacking lets us swap without temp variable.

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
a, b = b, a
print("After swapping: a =", a, ", b =", b)
