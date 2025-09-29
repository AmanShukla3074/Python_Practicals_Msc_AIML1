# 4.	Store a person’s contact info (name, phone, email) in a dictionary. Access the email.
# Answer:
# Simple mapping from keys to values.

name = input("Name: ")
phone = input("Phone: ")
email = input("Email: ")
contact = {"name": name, "phone": phone, "email": email}
print("Email is:", contact["email"])
