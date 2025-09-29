# 14.	Clear all entries from a dictionary of student grades.
# Answer:
# Use clear() to empty the dict.

pairs = input("Enter student:marks pairs comma separated: ")
grades = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
print("Before clearing:", grades)
grades.clear()
print("After clearing:", grades)
