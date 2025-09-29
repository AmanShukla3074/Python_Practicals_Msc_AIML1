# 4.	Give an example of implicit type conversion in Python.
# Answer:
# A common implicit conversion is int -> float when mixing types in arithmetic.

_ = input("Press Enter to see an implicit conversion example: ")
a = 5        # int
b = 2.5      # float
res = a + b  # int implicitly converted to float
print("5 (int) + 2.5 (float) =", res, "-> type:", type(res))
print("Explanation: int was implicitly converted to float so result is float.")
