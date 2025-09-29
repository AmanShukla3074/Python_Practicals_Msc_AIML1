# 2.	Write a Python program to find the common elements between two lists.
# Answer:
# I convert both inputs to lists and use a simple loop to collect common elements preserving order.

a = input("Enter elements of first list separated by spaces: ").split()
b = input("Enter elements of second list separated by spaces: ").split()

common = []
seen = set()
for x in a:
    if x in b and x not in seen:
        common.append(x)
        seen.add(x)

print("Common elements (order from first list):", common)
