# 8.	Find the index of element 25 in (10, 20, 25, 30, 25, 40).
# Answer:
# I use the index() method to get the first occurrence.

t = tuple(map(int, input("Enter numbers for the tuple: ").split()))
x = int(input("Enter element to find index: "))
if x in t:
    print("Index of", x, ":", t.index(x))
else:
    print(x, "not found in tuple.")
