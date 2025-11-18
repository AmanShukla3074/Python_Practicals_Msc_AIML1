# 16. Program to add two lists element-wise using lambda and map().
list1 = [1, 2, 3]
list2 = [4, 5, 6]
added = list(map(lambda a, b: a + b, list1, list2))
print(added)
