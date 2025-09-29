# 33.	Convert a list of temperatures in Celsius into a dictionary of Fahrenheit values.
# Answer:
# Formula F = C*9/5 + 32; map input list indices or values.

c_list = input("Enter Celsius temps separated by spaces: ").split()
c_vals = [float(x) for x in c_list]
f_dict = {c: (c * 9/5) + 32 for c in c_vals}
print("Celsius->Fahrenheit:", f_dict)
