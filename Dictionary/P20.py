# 20.	Iterate over employee IDs and names, printing each pair.
# Answer:
# Expect input like id:name pairs.

pairs = input("Enter id:name pairs comma separated: ")
emps = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
for emp_id, name in emps.items():
    print(f"ID {emp_id} -> {name}")
