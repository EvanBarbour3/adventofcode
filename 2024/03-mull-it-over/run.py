import re

f = open("input.txt", "r")
records = [line for line in f]


def fetch_mul_details(records) -> dict:
    rtn = {}
    regex = r"mul\((\d+),(\d+)\)"
    for i, record in enumerate(records):
        rtn.update(
            {
                (i, match.start()): (int(match.group(1)), int(match.group(2)))
                for match in re.finditer(regex, record)
            }
        )

    return rtn


def fetch_enablements(records) -> dict:
    rtn = {}
    regex = r"(do\(\)|don't\(\))"
    for i, record in enumerate(records):
        rtn.update(
            {(i, match.start()): match.group(1) for match in re.finditer(regex, record)}
        )

    return rtn


def challenge_1():
    total = 0
    mul = fetch_mul_details(records)
    for first, second in mul.values():
        total += first * second

    print(f"Answer 1: {total}")


def challenge_2():
    total = 0
    mul = fetch_mul_details(records)
    enablements = fetch_enablements(records)

    do = True
    for line in range(len(records)):
        # Filter to these mul's
        m = {key: value for key, value in mul.items() if key[0] == line}
        e = {key: value for key, value in enablements.items() if key[0] == line}

        # Merge and sort by the tuple second tuple value, the first value is the line and we're merging after that so sack it
        merged = {**m, **e}
        merged = {k: v for k, v in sorted(merged.items(), key=lambda item: item[0][1])}

        for _, v in merged.items():
            # enablement
            if isinstance(v, str):
                do = False if v == "don't()" else True
            # mul
            else:
                total += (v[0] * v[1]) if do else 0
                pass

    print(f"Answer 2: {total}")


challenge_1()
challenge_2()
