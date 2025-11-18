# 7. Write a function to generate the Fibonacci series up to n terms.
def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print(fibonacci(10))
