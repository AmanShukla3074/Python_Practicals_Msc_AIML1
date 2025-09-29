# 9.	Write a Python program to add two complex numbers.
# Answer:
# Complex numbers are supported natively with the 'complex' type.

a_str = input("Enter first complex number (e.g. 1+2j): ")
b_str = input("Enter second complex number (e.g. 3+4j): ")
a = complex(a_str)
b = complex(b_str)
print(f"{a} + {b} = {a + b}")
