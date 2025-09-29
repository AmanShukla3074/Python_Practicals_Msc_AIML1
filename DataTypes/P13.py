# 13.	Write a Python program to print the memory address of a variable.
# Answer:
# Use id() function to get the object's memory identity (address-like integer).

_ = input("Press Enter and then I'll show the memory id of an example variable: ")
x = input("Enter any value to inspect its memory id: ")
print("id(x) =", id(x))
print("Note: id() returns an integer unique during the object's lifetime.")
