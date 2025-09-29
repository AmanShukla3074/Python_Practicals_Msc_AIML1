# 20.	Write Python code to return the sum of all numbers in the tuple (1, 2, 3, 4, 5).
# Answer:
# I simply use the sum() function.

t = tuple(map(int, input("Enter numbers for the tuple: ").split()))
print("Sum of all numbers:", sum(t))
