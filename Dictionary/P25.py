# 25.	Determine if a student’s roll number is present in a class dictionary.
# Answer:
# Keys are roll numbers; check membership.

pairs = input("Enter roll:student pairs comma separated: ")
cls = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
roll = input("Enter roll number to check: ")
print("Present?" , roll in cls)
