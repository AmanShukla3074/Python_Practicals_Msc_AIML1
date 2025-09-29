# 20.	Write a Python program to find the k smallest elements in a list.
# Answer:
# I sort the list and take the first k unique/specified elements.

lst = input("Enter numbers separated by spaces: ").split()
nums = [float(x) for x in lst]
k = int(input("Enter k (number of smallest elements to find): "))

if k <= 0:
    print("k must be positive.")
else:
    sorted_nums = sorted(nums)
    result = sorted_nums[:k] if k <= len(sorted_nums) else sorted_nums
    print(f"{k} smallest elements:", result)
