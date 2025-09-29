# 10.	How can you extract real and imaginary parts of a complex number?
# Answer:
# Use .real and .imag attributes.

s = input("Enter a complex number (e.g. 2+3j): ")
z = complex(s)
print("Real part:", z.real)
print("Imag part:", z.imag)
