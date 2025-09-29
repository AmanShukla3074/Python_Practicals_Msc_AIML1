my_dict = {}

n = int(input("How many items do you want to add to the dictionary? "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    my_dict[key] = value

print("Your dictionary:", my_dict)

print("\nChoose an operation:")
print("1. Add item")
print("2. Remove item")
print("3. Update item")
print("4. Search for a key")
print("5. Display dictionary")
choice = input("Enter choice (1-5): ")

if choice == '1':
    key = input("Enter key to add: ")
    value = input("Enter value: ")
    my_dict[key] = value
    print("Item added.")
elif choice == '2':
    key = input("Enter key to remove: ")
    if key in my_dict:
        del my_dict[key]
        print("Item removed.")
    else:
        print("Key not found.")
elif choice == '3':
    key = input("Enter key to update: ")
    if key in my_dict:
        value = input("Enter new value: ")
        my_dict[key] = value
        print("Item updated.")
    else:
        print("Key not found.")
elif choice == '4':
    key = input("Enter key to search: ")
    if key in my_dict:
        print(f"Value: {my_dict[key]}")
    else:
        print("Key not found.")
elif choice == '5':
    print("Dictionary:", my_dict)
else:
    print("Invalid choice.")