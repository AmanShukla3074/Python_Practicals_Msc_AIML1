# 14.	Sort the tuple (5, 2, 9, 1) in ascending order (hint: convert to list first).
# Answer:
# Tuples can’t be sorted directly, so I convert to list and back.

t = tuple(map(int, input("Enter numbers for the tuple: ").split()))
lst = sorted(list(t))
t_sorted = tuple(lst)
print("Sorted tuple:", t_sorted)
