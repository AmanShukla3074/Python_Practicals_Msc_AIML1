# 19.	Given a list of tuples [("John", 90), ("Emma", 85), ("Bob", 95)], sort by marks in descending order.
# Answer:
# I use sorted() with key and reverse=True.

lst = eval(input("Enter list of (name, marks) tuples: "))
sorted_list = sorted(lst, key=lambda x: x[1], reverse=True)
print("Sorted by marks (descending):", sorted_list)
