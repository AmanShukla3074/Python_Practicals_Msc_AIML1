# 46.	Store stock prices of companies and print the company with the highest price.
# Answer:
# Read company:price pairs and find max by value.

pairs = input("Enter company:price pairs comma separated: ")
stocks = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
if stocks:
    top = max(stocks.items(), key=lambda x: x[1])
    print("Highest price company:", top[0], "with price", top[1])
else:
    print("No stocks provided.")
