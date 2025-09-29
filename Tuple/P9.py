# 9.	Count how many times 5 appears in (5, 10, 15, 5, 20, 5).
# Answer:
# I use the count() method of tuple.

t = tuple(map(int, input("Enter numbers for the tuple: ").split()))
x = int(input("Enter element to count: "))
print(x, "appears", t.count(x), "times.")
