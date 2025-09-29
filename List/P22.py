# 22.	Write a Python program to find the largest product of two distinct elements in a list.
# Answer:
# I consider largest and smallest numbers because two negatives can give a large positive.

lst = input("Enter numbers separated by spaces: ").split()
nums = [float(x) for x in lst]

if len(nums) < 2:
    print("Need at least two numbers.")
else:
    nums.sort()
    candidate1 = nums[0] * nums[1]          # two smallest (possibly negative)
    candidate2 = nums[-1] * nums[-2]      # two largest
    best = max(candidate1, candidate2)
    print("Largest product of two distinct elements is:", best)
