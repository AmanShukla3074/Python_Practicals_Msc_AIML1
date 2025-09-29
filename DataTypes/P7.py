# 7.	When should we use the decimal module instead of float?
# Answer:
# Use decimal for precise decimal arithmetic (money, exact base-10 calculations).

_ = input("Press Enter for a short example and explanation: ")
from decimal import Decimal
a = Decimal('1.1')
b = Decimal('2.2')
print("Decimal 1.1 + 2.2 =", a + b)
print("Use Decimal when you need exact base-10 results (e.g., currency).")
