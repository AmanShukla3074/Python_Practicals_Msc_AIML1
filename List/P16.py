# 16.	Write a Python program to find the median of a list.
# Answer:
# I sort the numbers and handle odd/even length cases.

lst = input("Enter numbers separated by spaces: ").split()
nums = [float(x) for x in lst]
n = len(nums)

if n == 0:
    print("No median for empty list.")
else:
    nums.sort()
    mid = n // 2
    if n % 2 == 1:
        median = nums[mid]
    else:
        median = (nums[mid-1] + nums[mid]) / 2
    print("Median is:", median)
