f = open("input.txt", "r")
records = [list(line.replace("\n", "")) for line in f]

word = "XMAS"
rows = len(records)
cols = len(records[0])


def find_xmas_sum(records):
    directions = [
        (-1, 0),  # N
        (0, 1),  # E
        (1, 0),  # S
        (0, -1),  # W
        (-1, 1),  # NE
        (1, 1),  # SE
        (-1, -1),  # NW
        (1, -1),  # SW
    ]

    total = 0

    def search(x, y, dirx, diry):
        # For each letter in the word XMAS
        for i in range(len(word)):
            # Find out the position, move in a direction for both x and y
            pos_x = x + (i * dirx)
            pos_y = y + (i * diry)
            # Check we can go there first, and then check the pos is the letter of the word
            if not valid_pos(pos_x, pos_y) or records[pos_x][pos_y] != word[i]:
                return False
        return True

    # Loop rows
    for row_i in range(0, rows):
        # Each col
        for col_i in range(0, cols):
            # Check if the word is in the specific position @ direction of what we're checking
            for dir_x, dir_y in directions:
                total += 1 if search(row_i, col_i, dir_x, dir_y) else 0

    return total


# Check the position is actually in the grid, dont go out of it else error
def valid_pos(pos_x, pos_y):
    return 0 <= pos_x < rows and 0 <= pos_y < cols


def find_mas_sum(records):
    total = 0
    directions = {
        (-1, 1): (1, -1),  # NE opposide = SW
        (1, 1): (-1, -1),  # SE opposite = NW
    }
    opposites = {
        "S": "M",
        "M": "S",
    }

    def search_corners(corner_1_x, corner_1_y, corner_2_x, corner_2_y) -> bool:
        success = 2
        if valid_pos(corner_1_x, corner_1_y) and valid_pos(corner_2_x, corner_2_y):
            letter = records[corner_1_x][corner_1_y]
            # The letter is an S or an M
            if letter in opposites:
                # Now check the opposite corner to see if that's also the opposite for the S or the M
                return (
                    True
                    if records[corner_2_x][corner_2_y] == opposites[letter]
                    else False
                )

        return success == 0

    for row_i in range(0, rows):
        # Each col
        for col_i in range(0, cols):
            # Check if the pos is an A
            if valid_pos(row_i, col_i) and records[row_i][col_i] == "A":
                # Now we can check either direction
                success = 2
                for corner_one, corner_two in directions.items():
                    corner_1_x = row_i + corner_one[0]
                    corner_1_y = col_i + corner_one[1]
                    corner_2_x = row_i + corner_two[0]
                    corner_2_y = col_i + corner_two[1]

                    success += (
                        -1
                        if search_corners(
                            corner_1_x, corner_1_y, corner_2_x, corner_2_y
                        )
                        else 0
                    )

                total += 1 if success == 0 else 0

    return total


def challenge_1():
    print(f"Answer 1: {find_xmas_sum(records)}")


def challenge_2():
    print(f"Answer 2: {find_mas_sum(records)}")


challenge_1()
challenge_2()
