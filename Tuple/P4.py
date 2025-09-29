# 4.	Can you change the 2nd element of a tuple (100, 200, 300)? Why or why not?
# Answer:
# No, tuples are immutable. We cannot directly change their elements.

t = tuple(map(int, input("Enter numbers for the tuple: ").split()))
try:
    t[1] = 999
except TypeError:
    print("Tuples are immutable, you cannot change elements directly.")
