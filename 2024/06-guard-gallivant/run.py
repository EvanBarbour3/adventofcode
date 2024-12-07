import copy

f = open("input.txt", "r")
records = [list(line.replace("\n", "")) for line in f]
rows = len(records)
cols = len(records[0])

directions = [
    [-1, 0],  # up
    [0, 1],  # right
    [1, 0],  # down
    [0, -1],  # left
]


def print_map(map):
    for x in map:
        print(x)


def walk(startx, starty, map, breakpoint):
    curr = 0
    map = map
    direction = 0
    x = startx
    y = starty

    while valid_pos(x, y):
        if curr > breakpoint:
            raise Exception("Infinite loop")

        # Debug, check to see working
        # print_map(map)
        # Straight up, we're off the map
        if not valid_pos(x + directions[direction][0], y + directions[direction][1]):
            map[x][y] = "X"
            return map

        # Next position is not a #, lets move to it
        if (
            valid_pos(x, y)
            and map[x + directions[direction][0]][y + directions[direction][1]] != "#"
        ):
            map[x][y] = "X"
            map[x + directions[direction][0]][y + directions[direction][1]] = "*"
        # Next pos is a #, lets swap direction
        else:
            if direction == 3:
                direction = 0
            else:
                direction += 1

        # Find the new pos we're at
        new = find_guard(map, "*")
        x = new[0]
        y = new[1]

        curr += 1

    return map


# Check the position is actually in the grid, dont go out of it else error
def valid_pos(pos_x, pos_y):
    return 0 <= pos_x < rows and 0 <= pos_y < cols


def find_guard(map, target):
    for x, row in enumerate(map):
        for y, value in enumerate(row):
            if value == target:
                return (x, y)


def find_breakpoint(map):
    return sum(len(row) for row in map)


start = find_guard(records, "^")
# Change the guard to a *
records[start[0]][start[1]] = "*"
breakpoint = find_breakpoint(records)
records_og = copy.deepcopy(records)
final = walk(start[0], start[1], records, breakpoint)


def challenge_1():
    final = walk(start[0], start[1], records, breakpoint)
    print(f"Answer 1: {sum(row.count('X') for row in final)}")


def challenge_2():
    total = 0
    for ri, row in enumerate(final):
        print(f"Running row {ri}")
        for ii, item in enumerate(row):
            if item == "." or item == "#":
                continue

            if ri == start[0] and ii == start[1]:
                continue

            new_final = copy.deepcopy(final)
            new_final[ri][ii] = "#"
            new_final[start[0]][start[1]] = "*"

            try:

                walk(start[0], start[1], new_final, breakpoint)
            except Exception as e:

                total += 1

    print(f"Answer 2: {total}")


challenge_1()
challenge_2()
