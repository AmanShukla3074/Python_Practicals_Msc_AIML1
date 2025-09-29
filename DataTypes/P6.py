# 6.	Why does 1.1 + 2.2 not exactly equal 3.3 in Python?
# Answer:
# Because floats are binary approximations and some decimals can't be represented exactly.

_ = input("Press Enter to see the demonstration: ")
print("Demonstration:")
print("1.1 + 2.2 =", 1.1 + 2.2)
print("3.3      =", 3.3)
print("So 1.1 + 2.2 == 3.3 ? ->", (1.1 + 2.2) == 3.3)
print("Explanation: floating-point rounding/representation error in binary.")
