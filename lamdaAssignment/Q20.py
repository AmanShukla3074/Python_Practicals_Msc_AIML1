# 20. Program to categorize a number as positive, negative, or zero using lambda with conditional expressions.
categorize = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")
print(categorize(-5))
