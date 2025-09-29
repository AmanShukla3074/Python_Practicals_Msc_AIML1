# 35.	Make a dictionary of employees and assign "active" status to all.
# Answer:
# Read employee names and set status "active".

emps = input("Enter employee names separated by commas: ").split(',')
status = {e.strip(): "active" for e in emps if e.strip()}
print("Employee statuses:", status)
