# 12.	Delete an employee record by key from a company dictionary.
# Answer:
# Remove a key provided by user if it exists.

pairs = input("Enter emp:salary pairs comma separated: ")
company = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
key = input("Employee key to delete: ")
if key in company:
    del company[key]
    print(key, "deleted.")
else:
    print(key, "not found.")
print("Company dict:", company)
