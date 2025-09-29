# 24.	Write a Python program to find the difference between consecutive elements in a list.
# Answer:
# I compute element[i+1] - element[i] for each consecutive pair.

lst = input("Enter numbers separated by spaces: ").split()
nums = [float(x) for x in lst]

if len(nums) < 2:
    print("Need at least two numbers to compute differences.")
else:
    diffs = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    print("Differences between consecutive elements:", diffs)
