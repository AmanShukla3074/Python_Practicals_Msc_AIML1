# 12.	Write a Python program to swap two variables without a temporary variable.
# Answer:
# Python tuple unpacking makes swap simple: a, b = b, a

a = input("Enter value for a: ")
b = input("Enter value for b: ")
print("Before swap: a =", a, ", b =", b)
a, b = b, a
print("After swap: a =", a, ", b =", b)
