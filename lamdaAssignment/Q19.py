# 19. Program to sort a list of tuples in descending order by second element using lambda.
data = [(1, 5), (3, 1), (2, 4)]
sorted_desc = sorted(data, key=lambda x: x[1], reverse=True)
print(sorted_desc)
