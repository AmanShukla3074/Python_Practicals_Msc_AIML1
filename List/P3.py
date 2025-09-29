# 3.	Write a Python program to find the common elements between two lists without using loops.
# Answer:
# I used set intersection which finds common elements without explicit loops.

a = input("Enter elements of first list separated by spaces: ").split()
b = input("Enter elements of second list separated by spaces: ").split()

common = list(set(a).intersection(b))
print("Common elements (unordered):", common)
