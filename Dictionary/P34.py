# 34.	Create a dictionary mapping numbers to "even" or "odd".
# Answer:
# For numbers in a given range or list, mark parity.

nums = input("Enter integers separated by spaces: ").split()
nums = [int(x) for x in nums]
parity = {n: ("even" if n % 2 == 0 else "odd") for n in nums}
print("Parity dict:", parity)
