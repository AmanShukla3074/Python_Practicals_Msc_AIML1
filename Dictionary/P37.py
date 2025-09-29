# 37.	Store multiple bank accounts in a dictionary with details (balance, type).
# Answer:
# Accounts keyed by account number with nested dicts.

n = int(input("How many accounts? "))
accounts = {}
for i in range(n):
    acc = input("Account number: ")
    bal = float(input("Balance: "))
    typ = input("Type (savings/current): ")
    accounts[acc] = {"balance": bal, "type": typ}
print("Accounts:", accounts)
