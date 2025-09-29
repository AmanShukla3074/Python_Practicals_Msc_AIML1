# 7.	Repeat the tuple (7, 8) three times.
# Answer:
# I use the * operator to repeat.

t = tuple(map(int, input("Enter numbers for the tuple: ").split()))
n = int(input("Enter number of times to repeat: "))
print("Repeated tuple:", t * n)
