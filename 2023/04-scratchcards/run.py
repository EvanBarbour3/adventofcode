import re

f = open("input.txt", "r")

records = []

for x in f:
    result = re.search(r"Card.*?(\d+): (.*?) \| (.*)", x.strip())
    game = int(result.group(1))
    winning = [int(x) for x in filter(len, result.group(2).split(" "))]
    mine = [int(x) for x in filter(len, result.group(3).split(" "))]

    records.append(
        {
            "game": game,
            "winning": winning,
            "mine": mine,
            "result": list(set(winning) & set(mine)),
            "how_many_of": 1,
        }
    )

print(
    f'Answer 1: {sum(list(map(lambda x: pow(2, x-1), [i for i in list(map(lambda x: len(x["result"]), records )) if i != 0])))}'
)

for idx, record in enumerate(records):
    for i in range(idx + 1, idx + 1 + len(record["result"])):
        try:
            records[i]["how_many_of"] += record["how_many_of"]
        except IndexError:
            pass


print(f'Answer 2: {sum(list(map(lambda x: x["how_many_of"], records)))}')
