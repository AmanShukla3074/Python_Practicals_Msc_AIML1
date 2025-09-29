# 50.	Store train schedules (train_no: time) and print all trains after 6 PM.
# Answer:
# Expect times in HH:MM 24-hour format and filter > 18:00.

pairs = input("Enter train:HH:MM pairs comma separated (e.g. 123:17:30,234:18:45): ")
schedules = {}
for p in pairs.split(','):
    if p.strip():
        tkn = p.split(':')
        # allow train_no:HH:MM where split by ':' yields at least 3 parts
        train = tkn[0].strip()
        time = ":".join(tkn[1:]).strip()
        schedules[train] = time
print("Trains after 18:00:")
for tr, tm in schedules.items():
    hh, mm = map(int, tm.split(':'))
    if hh >= 18 and (hh > 18 or mm > 0):
        print(tr, "at", tm)
