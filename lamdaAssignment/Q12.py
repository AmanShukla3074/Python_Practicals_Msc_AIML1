# 12. Program to create a multiplier function using a nested lambda.
multiplier = lambda n: (lambda x: x * n)
double = multiplier(2)
print(double(10))
