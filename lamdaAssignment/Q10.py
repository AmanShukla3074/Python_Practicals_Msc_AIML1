# 10. Program to perform arithmetic operations (add, subtract, multiply) using lambda in a dictionary.
ops = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b
}
print(ops["add"](5, 3), ops["sub"](5, 3), ops["mul"](5, 3))
