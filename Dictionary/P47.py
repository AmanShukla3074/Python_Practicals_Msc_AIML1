# 47.	Store subjects and marks, then calculate total and average.
# Answer:
# Sum values and compute average.

pairs = input("Enter subject:marks pairs comma separated: ")
subs = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
total = sum(subs.values())
avg = total / len(subs) if subs else 0
print("Total:", total, "Average:", avg)
