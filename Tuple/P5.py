# 5.	Write code to check whether 50 exists in the tuple (10, 20, 30, 40, 50).
# Answer:
# I use the `in` operator to check membership.

t = tuple(map(int, input("Enter numbers for the tuple: ").split()))
x = int(input("Enter number to check: "))
print(x, "exists in tuple?" , (x in t))
