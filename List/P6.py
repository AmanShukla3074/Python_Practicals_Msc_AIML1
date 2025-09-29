# 6.	Write a Python program to find the product of all elements in a list.
# Answer:
# I use math.prod if available; otherwise fall back to a simple loop.

import math
lst = input("Enter numbers separated by spaces: ").split()
nums = [float(x) for x in lst]

try:
    prod = math.prod(nums)
except AttributeError:
    prod = 1
    for n in nums:
        prod *= n

print("Product of all elements:", prod)
