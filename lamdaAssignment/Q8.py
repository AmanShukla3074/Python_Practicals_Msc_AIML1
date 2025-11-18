# 8. Program to find the sum of all elements in a list using lambda and reduce().
from functools import reduce
nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, nums)
print(total)
