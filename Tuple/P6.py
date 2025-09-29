# 6.	Concatenate two tuples (1, 2, 3) and (4, 5, 6).
# Answer:
# Tuples can be joined using the + operator.

t1 = tuple(map(int, input("Enter numbers for first tuple: ").split()))
t2 = tuple(map(int, input("Enter numbers for second tuple: ").split()))
print("Concatenated tuple:", t1 + t2)
