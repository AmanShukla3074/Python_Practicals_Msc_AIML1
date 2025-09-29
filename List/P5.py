# 5.	Write a Python program to check if a list is empty.
# Answer:
# I just check truthiness of the list and print a friendly message.

lst = input("Enter elements separated by spaces (leave blank for empty list): ").strip()
if lst == "":
    the_list = []
else:
    the_list = lst.split()

if the_list:
    print("List is not empty. It has", len(the_list), "elements.")
else:
    print("List is empty.")
