from functools import reduce
import re

with open("input.txt", "r") as f:
    data = f.read()

x = re.search(
    r"Time:(.*?)\nDistance:(.*)",
    data,
)


def mapfirstinputs(s: str) -> list:
    return list(map(int, list(filter(None, s))))


def mapsecondinputs(l: list) -> int:
    return int(reduce(lambda x, y: str(x) + str(y), l))


def howmanyways(time: int, distance: int) -> int:
    waystowin = 0

    for speed in range(0, time + 1):
        left = time - speed

        if speed * left > distance:
            waystowin += 1

    return waystowin


times = mapfirstinputs(x.group(1).split(" "))
distances = mapfirstinputs(x.group(2).split(" "))

first = []
for idx, time in enumerate(times):
    first.append(howmanyways(time, distances[idx]))

print(f"Answer 1: {reduce(lambda x, y: x*y, first)}")
print(f"Answer 2: {howmanyways(mapsecondinputs(times), mapsecondinputs(distances))}")
