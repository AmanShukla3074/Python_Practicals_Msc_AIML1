# 49.	Manage a to-do list with tasks and statuses (done/pending) using a dictionary.
# Answer:
# Read tasks and statuses, then show summary and pending tasks.

pairs = input("Enter task:status pairs comma separated (status 'done' or 'pending'): ")
todo = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
print("To-do list:")
for t, s in todo.items():
    print(f"{t} -> {s}")
pending = [t for t, s in todo.items() if s.lower() != "done"]
print("Pending tasks:", pending)
