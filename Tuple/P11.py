# 11.	Access the value 20 from the tuple (10, (20, 30), 40).
# Answer:
# I use nested indexing: t[1][0].

t = eval(input("Enter a tuple (e.g. (10,(20,30),40)): "))
print("Accessed value:", t[1][0])
