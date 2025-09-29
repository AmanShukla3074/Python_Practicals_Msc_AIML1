# 26.	Store votes for candidates in an election. Count and print results.
# Answer:
# User supplies votes (candidate names). Count via dict.

votes = input("Enter votes separated by spaces (candidate names): ").split()
counts = {}
for v in votes:
    counts[v] = counts.get(v, 0) + 1
print("Vote counts:")
for cand, c in counts.items():
    print(cand, ":", c)
