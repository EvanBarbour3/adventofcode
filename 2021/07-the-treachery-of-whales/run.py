f = open("input.txt", "r")

records = []

for x in f:
    records.append(x.strip())

records = [int(x) for x in records[0].split(",")]

first = []
second = []
for i in range(min(records), max(records) + 1):
    f = 0
    s = 0

    for e in records:
        f += abs(i - e)
        s += sum([x for x in range(0, abs(i - e) + 1)])

    first.append(f)
    second.append(s)

print(f"Answer 1: {min(first)}")
print(f"Answer 2: {min(second)}")
