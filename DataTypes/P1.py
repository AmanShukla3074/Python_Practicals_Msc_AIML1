# 1.	Write a Python program to check if a given string is a valid identifier.
# Answer:
# I'll use str.isidentifier() which directly tells us if a string is a valid Python identifier.

s = input("Enter a string to check if it's a valid identifier: ")
print("Simple human answer: checking with isidentifier() ...")
print(f"Is '{s}' a valid identifier? ->", s.isidentifier())



# # 1.	Write a Python program to display the type of a variable.
# # Answer:
# # Use type() to display the variable's type. (Note: this question appears numbered '1.' in the list.)

# _ = input("Press Enter and then input a value to check its type: ")
# val = input("Enter something (it will be treated as string input): ")
# # We will try to infer simple types (int/float) then show type
# try:
#     v_eval = int(val)
#     print(val, "looks like an int -> type:", type(v_eval))
# except:
#     try:
#         v_eval = float(val)
#         print(val, "looks like a float -> type:", type(v_eval))
#     except:
#         print(val, "is a string -> type:", type(val))
