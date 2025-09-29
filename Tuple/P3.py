# 3.	Write Python code to slice a tuple (1, 2, 3, 4, 5, 6) to get (3, 4, 5).
# Answer:
# I use slicing: t[2:5].

t = tuple(map(int, input("Enter numbers for the tuple: ").split()))
print("Slice (3rd to 5th elements):", t[2:5])
