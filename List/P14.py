# 14.	Write a Python program to split a list for a given number of lists.
# Answer:
# I split into k nearly equal parts, distributing extra elements to the first parts.

lst = input("Enter elements separated by spaces: ").split()
k = int(input("Enter number of lists to split into (k): "))

n = len(lst)
if k <= 0:
    print("k must be positive.")
else:
    base = n // k
    extra = n % k
    result = []
    idx = 0
    for i in range(k):
        size = base + (1 if i < extra else 0)
        result.append(lst[idx:idx+size])
        idx += size
    print("Split into", k, "lists:")
    for i, part in enumerate(result, 1):
        print(f"Part {i}:", part)
