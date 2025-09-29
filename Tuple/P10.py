# 10.	Write a program to convert a tuple (1, 2, 3) into a list, append 4, and convert back to a tuple.
# Answer:
# I convert to list, append, then convert back.

t = tuple(map(int, input("Enter numbers for the tuple: ").split()))
lst = list(t)
val = int(input("Enter value to append: "))
lst.append(val)
t = tuple(lst)
print("Tuple after append:", t)
