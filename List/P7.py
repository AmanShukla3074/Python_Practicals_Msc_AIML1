# 7.	Write a Python program to rotate a list to the right by n positions.
# Answer:
# I use slicing to rotate the list to the right.

lst = input("Enter elements separated by spaces: ").split()
n = int(input("Enter number of positions to rotate right (n): "))

if not lst:
    print("Empty list remains empty.")
else:
    n = n % len(lst)
    rotated = lst[-n:] + lst[:-n] if n else lst[:]
    print("Rotated list:", rotated)
