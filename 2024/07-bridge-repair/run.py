records = []
[records.append(line) for line in open("input.txt", "r")]

parsed = []
for record in records:
    record = record.strip()
    total, numbers = record.split(": ")
    parsed.append((int(total), list(map(int, numbers.split()))))


def can_make_total(numbers, total, allow_concat: False):
    def recurse(index, current_value):
        # we've done all numbers
        if index == len(numbers):
            return current_value == total

        next_num = numbers[index]

        # try + and * and ||
        if allow_concat:
            return (
                recurse(index + 1, current_value + next_num)
                or recurse(index + 1, current_value * next_num)
                or recurse(index + 1, int(str(current_value) + str(next_num)))
            )
        # try + and *
        else:
            return recurse(index + 1, current_value + next_num) or recurse(
                index + 1, current_value * next_num
            )

    return recurse(1, numbers[0])


def challenge_1():
    possible = 0
    for equation in parsed:
        if can_make_total(equation[1], equation[0], False):
            possible += equation[0]

    print(f"Answer 1: {possible}")


def challenge_2():
    possible = 0
    for equation in parsed:
        if can_make_total(equation[1], equation[0], True):
            possible += equation[0]

    print(f"Answer 2: {possible}")


challenge_1()
challenge_2()
