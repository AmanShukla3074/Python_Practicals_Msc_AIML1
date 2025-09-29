# 28.	Count how many students scored above 80 in a marks dictionary.
# Answer:
# Read name:marks and count marks>80.

pairs = input("Enter name:marks pairs comma separated: ")
marks = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
count = sum(1 for m in marks.values() if m > 80)
print("Students scoring above 80:", count)
