# 10.	Write a Python program to shuffle a list randomly.
# Answer:
# I use random.shuffle in place to shuffle the list.

import random
lst = input("Enter elements separated by spaces: ").split()
random.shuffle(lst)
print("Shuffled list:", lst)
