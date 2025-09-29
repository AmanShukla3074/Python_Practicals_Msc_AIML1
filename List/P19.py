# 19.	Write a Python program to find the common elements among three lists.
# Answer:
# I use set intersection to find elements common to all three.

a = input("Enter elements of first list separated by spaces: ").split()
b = input("Enter elements of second list separated by spaces: ").split()
c = input("Enter elements of third list separated by spaces: ").split()

common = list(set(a).intersection(b).intersection(c))
print("Common elements among the three lists:", common)
