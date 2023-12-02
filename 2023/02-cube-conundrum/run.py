import re

f = open("input.txt", "r")
records = []

for x in f:
    records.append(x)


def parse(line: str, challenge: int):
    r = 1
    g = 1
    b = 1

    result = re.search(r"Game (\d+): (.*)", line.strip())
    game = int(result.group(1))
    combos = result.group(2).split("; ")
    possible = True

    for combo in combos:
        for selection in combo.split(", "):
            picked_result = re.search(r"(\d+) (.*)", selection)
            many = int(picked_result.group(1))
            match picked_result.group(2):
                case "red":
                    r = max(r, many)
                    if many > 12:
                        possible = False
                case "green":
                    g = max(g, many)
                    if many > 13:
                        possible = False
                case "blue":
                    b = max(b, many)
                    if many > 14:
                        possible = False

    if challenge == 1:
        if possible:
            return game
        else:
            return 0
    else:
        return r * g * b


def challenge_1():
    print(f"Answer 1: {sum([parse(x, 1) for x in records])}")


def challenge_2():
    print(f"Answer 2: {sum([parse(x, 2) for x in records])}")


challenge_1()
challenge_2()
