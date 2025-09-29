# 8.	Give an example of creating a Fraction from a string.
# Answer:
# fractions.Fraction can parse string like '3/4' or '1.5'.

s = input("Enter a fraction string (e.g. '3/4' or '1.5'): ")
from fractions import Fraction
try:
    f = Fraction(s)
    print("Created Fraction:", f)
except Exception as e:
    print("Could not create Fraction:", e)
