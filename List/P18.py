# 18.	Write a Python program to find the sum of elements at odd indices in a list.
# Answer:
# I sum items that appear at indices 1,3,5,... using enumerate.

lst = input("Enter numbers separated by spaces: ").split()
nums = [float(x) for x in lst]
s = sum(val for i, val in enumerate(nums) if i % 2 == 1)
print("Sum of elements at odd indices:", s)
