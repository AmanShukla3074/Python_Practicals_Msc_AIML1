# 18. Program to demonstrate a nested lambda expression (lambda returning another lambda).
nested = lambda a: (lambda b: a + b)
func = nested(10)
print(func(5))
