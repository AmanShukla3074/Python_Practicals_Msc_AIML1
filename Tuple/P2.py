# 2.	How do you access the 3rd element from the tuple (10, 20, 30, 40, 50)?
# Answer:
# Tuples are indexed from 0, so the 3rd element is at index 2.

t = tuple(map(int, input("Enter numbers for the tuple: ").split()))
if len(t) >= 3:
    print("3rd element is:", t[2])
else:
    print("Tuple has less than 3 elements.")
