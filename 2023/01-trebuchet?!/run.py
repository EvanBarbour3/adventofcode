f = open("input.txt", "r")
records = []

for x in f:
    records.append(x)

mapping = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}


def find_calibration_value(line: str) -> int:
    local = ""

    # Forwards
    for i in line:
        if i.isdigit():
            local = local + i
            break
    # Backwards
    for i in reversed(line):
        if i.isdigit():
            local = local + i
            break

    return int(local)


def translate_line(line: str):
    for key, value in mapping.items():
        line = line.replace(key, value)

    return line


def challenge_1():
    print(f"Answer 1: {sum([find_calibration_value(x) for x in records])}")


def challenge_2():
    print(f"Answer 2: {sum([find_calibration_value(translate_line(x)) for x in records])}")


challenge_1()
challenge_2()
