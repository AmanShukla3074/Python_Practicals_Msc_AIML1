# 48.	Create a dictionary of contacts and allow the user to search by name.
# Answer:
# Build contacts and prompt for name to lookup.

pairs = input("Enter name:phone pairs comma separated: ")
contacts = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
query = input("Enter name to search: ")
print("Result:", contacts.get(query, "Contact not found"))
