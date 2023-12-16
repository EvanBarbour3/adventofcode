import math
import re

with open("input.txt", "r") as f:
    data = f.read()

x = re.search(
    r"(.*?)\n\n([\s\S]*.*)",
    data,
)

records = {}
for r in x.group(2).split("\n"):
    ri = re.search(r"(.*?) = \((.*?), (.*?)\)", r)
    records.update({ri.group(1): {"L": ri.group(2), "R": ri.group(3)}})


def howmanysteps(where: str, triplez=True):
    count = 0
    while True:
        for direction in list(x.group(1)):
            count += 1
            old = where
            where = records[old][direction]

            if triplez and where == "ZZZ":
                return count
            if not triplez and where.endswith("Z"):
                return count


print(f"Answers 1: {howmanysteps('AAA', True)}")

rtn = 1
for record in records:
    if record.endswith("A"):
        rtn = math.lcm(rtn, howmanysteps(record, False))

print(f"Answer 2: {rtn}")
