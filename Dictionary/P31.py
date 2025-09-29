# 31.	Create a dictionary of squares {1:1, 2:4, …, 10:100}.
# Answer:
# Use a loop to build squares.

squares = {i: i*i for i in range(1, 11)}
print("Squares dict:", squares)
