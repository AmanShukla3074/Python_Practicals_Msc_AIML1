# 16.	Print all student names and their marks from a marks dictionary.
# Answer:
# Iterate and print each pair.

pairs = input("Enter student:marks pairs comma separated: ")
marks = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
print("Student -> Marks:")
for name, m in marks.items():
    print(f"{name} -> {m}")
