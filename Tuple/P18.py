# 18.	Given a dictionary {"a": 1, "b": 2}, convert it into a list of tuples [("a", 1), ("b", 2)].
# Answer:
# I use dict.items() to get tuple pairs.

d = eval(input("Enter a dictionary: "))
result = list(d.items())
print("List of tuples:", result)
