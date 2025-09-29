# 12.	Write a Python program to find the longest consecutive sequence of elements in a list.
# Answer:
# Similar to previous, but I return the actual sequence (as a list).

lst = input("Enter integers separated by spaces: ").split()
nums = [int(x) for x in lst]

if not nums:
    print("No sequence (empty list).")
else:
    s = set(nums)
    best_seq = []
    for num in s:
        if num - 1 not in s:
            current = num
            seq = [current]
            while current + 1 in s:
                current += 1
                seq.append(current)
            if len(seq) > len(best_seq):
                best_seq = seq
    print("Longest consecutive sequence:", best_seq)
