f = open("input.txt", "r")
records = [tuple(map(int, line.split())) for line in f]


def validate_safe(report):
    # If all increasing, or all decreasing
    if all(report[i] < report[i + 1] for i in range(len(report) - 1)) or all(
        report[i] > report[i + 1] for i in range(len(report) - 1)
    ):
        # If the increase or decrease is between 1 and 3
        return (
            1
            <= max([abs(report[i] - report[i + 1]) for i in range(len(report) - 1)])
            <= 3
        )

    return False


def challenge_1():
    safe = 0
    for record in records:
        safe += 1 if validate_safe(record) else 0

    print(f"Answer 1: {safe}")


def challenge_2():
    safe = 0
    levels = len(records[0])
    for record in records:

        already = validate_safe(record)

        # if it's already safe without the dampener
        if already:
            safe += 1
            continue

        # Introduce the dampener and remove a level
        else:
            # Remove each level to make a new report, and check if that's safe
            for l in range(0, levels):
                new_record = record[:l] + record[l + 1 :]
                if validate_safe(new_record):
                    safe += 1
                    break

    print(f"Answer 2: {safe}")


challenge_1()
challenge_2()
