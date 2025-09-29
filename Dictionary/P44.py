# 44.	Turn a dictionary of marks into two separate lists: names and marks.
# Answer:
# Read name:marks pairs and unzip into two lists.

pairs = input("Enter name:marks pairs comma separated: ")
d = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
names = list(d.keys())
marks = list(d.values())
print("Names:", names)
print("Marks:", marks)
