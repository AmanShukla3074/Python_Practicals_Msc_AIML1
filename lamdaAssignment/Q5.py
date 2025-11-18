# 5. Program to sort a list of tuples based on the second element using lambda.
data = [(1, 5), (3, 1), (2, 4)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
