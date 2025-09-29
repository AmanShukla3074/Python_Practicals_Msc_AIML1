# 5.	Write a Python program to convert a float to an integer and explain the result.
# Answer:
# Converting float to int truncates (drops) the fractional part.

f = float(input("Enter a float value (e.g. 3.7): "))
i = int(f)
print(f"float {f} converted to int gives {i}")
print("Note: int() truncates toward zero — it does not round.")
