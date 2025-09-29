# 1.	Create a tuple with numbers 1, 2, 3, 4, 5 and print its length
# Answer:
# I just create the tuple and use len() to find its length.

t = tuple(map(int, input("Enter numbers for the tuple separated by spaces (e.g. 1 2 3 4 5): ").split()))
print("Length of the tuple:", len(t))
