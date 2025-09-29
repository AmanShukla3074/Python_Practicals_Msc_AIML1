# 11.	Write a Python program to find the length of the longest consecutive sequence of elements in a list.
# Answer:
# I use a set for O(n) detection of sequence starts and measure lengths.

lst = input("Enter integers separated by spaces: ").split()
nums = [int(x) for x in lst]

if not nums:
    print("Length of longest consecutive sequence: 0")
else:
    s = set(nums)
    best = 0
    for num in s:
        if num - 1 not in s:  # start of sequence
            length = 1
            current = num
            while current + 1 in s:
                current += 1
                length += 1
            if length > best:
                best = length
    print("Length of longest consecutive sequence:", best)
