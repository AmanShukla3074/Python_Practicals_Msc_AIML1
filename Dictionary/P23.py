# 23.	Check if a given phone number exists in a contact dictionary.
# Answer:
# Search values for presence of the phone number.

pairs = input("Enter name:phone pairs comma separated: ")
contacts = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
phone = input("Enter phone number to search: ")
exists = phone in contacts.values()
print("Phone exists in contacts?:", exists)
