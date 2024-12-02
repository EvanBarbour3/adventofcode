f = open("input.txt", "r")
records = [tuple(map(int, line.split())) for line in f]


list_l = [record[0] for record in records]
list_l.sort()
list_r = [record[1] for record in records]
list_r.sort()


def challenge_1():
    total = 0
    for left, right in zip(list_l, list_r):
        total += abs(left - right)

    print(f"Answer 1: {total}")


def challenge_2():
    total = 0
    total += sum([list_r.count(left) * left for left in list_l])

    print(f"Answer 2: {total}")


challenge_1()
challenge_2()
