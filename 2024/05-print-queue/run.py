from collections import defaultdict, deque
import re


with open("input.txt", "r") as f:
    data = f.read()

x = re.search(
    r"([\d\D]*.*)\n\n([\d\D]*.*)",
    data,
)

ordering = list(
    map(
        lambda i2: [int(i2[0]), int(i2[1])],
        map(lambda i: i.split("|"), x.group(1).replace("\n", " ").split(" ")),
    )
)
ordering_reverse = [r[::-1] for r in ordering]
updates = list(
    map(
        lambda i2: [int(i2[idx]) for idx in range(len(i2))],
        map(lambda i: i.split(","), x.group(2).replace("\n", " ").split(" ")),
    )
)

# print(ordering)
# print(updates)


def is_already_ordered(update):
    # print(update)
    # forward
    for i in update:
        forward_checks = list(filter(lambda order: order[0] == i, ordering))
        # print(forward_checks)
        # exit()
        backwards_checks = list(filter(lambda order: order[0] == i, ordering_reverse))

        # for x in forward_checks:
        #     print("checking backwards")
        #     print(x[1])

        if not all([check(update, i, x[1]) for x in forward_checks]) and all(
            [check(update, x[1], i) for x in backwards_checks]
        ):
            return False

    return True


def check(update, before_num, after_num) -> bool:
    try:
        if update.index(before_num) < update.index(after_num):
            return True
        else:
            pass
    except ValueError as _:
        return True

    return False


def sort_update(orderings, update):
    graph = defaultdict(list)
    degree = defaultdict(int)

    all_pages = set(update)
    for a, b in orderings:
        all_pages.update([a, b])
        graph[a].append(b)
        degree[b] += 1
        if a not in degree:
            degree[a] = 0

    # Start with nodes in 'update' that have zero in-degree
    queue = deque([page for page in update if degree[page] == 0])

    # Topological sort
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        # Decrease in-degree of neighbors
        for neighbor in graph[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                queue.append(neighbor)

    print(result)
    return result


def get_middle(lst):
    mid_idx = len(lst) // 2
    return lst[mid_idx]


# correct = []
# [correct.append(update) for update in updates if is_already_ordered(update)]
# print(sum(get_middle(update) for update in correct))
# print(correct)


def challenge_1():
    correct = []
    [correct.append(update) for update in updates if is_already_ordered(update)]

    print(f"Answer 1: {sum(get_middle(update) for update in correct)}")


def challenge_2():
    incorrect = []
    [incorrect.append(update) for update in updates if not is_already_ordered(update)]

    new = []

    print((ordering))
    print("\n")
    print(updates[0])
    # for update in incorrect:
    [new.append(sort_update((ordering), update)) for update in incorrect]

    print(f"Answer 2: {sum(get_middle(update) for update in new)}")


challenge_1()

challenge_2()
