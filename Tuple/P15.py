# 15.	Given two lists ["a", "b", "c"] and [1, 2, 3], create a list of tuples like [("a",1), ("b",2), ("c",3)].
# Answer:
# I use the zip() function.

l1 = input("Enter elements of first list separated by spaces: ").split()
l2 = input("Enter elements of second list separated by spaces: ").split()
result = list(zip(l1, l2))
print("List of tuples:", result)
