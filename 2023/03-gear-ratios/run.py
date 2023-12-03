import copy
from functools import reduce

f = open("input.txt", "r")

records = []
all_symbols = []
template = {"number": "", "positions": list(), "row": 0}

for x in f:
    records.append([c for c in x.strip()])

    # Get every char which isn't "0123456789."
    for c in x.strip():
        if not c.isdigit() and c != "." and c not in all_symbols:
            all_symbols.append(c)

mapped_numbers = []
mapped_symbol = []
for row_index, row in enumerate(records):
    temp = copy.deepcopy(template)
    temp["row"] = row_index
    for ch_index, ch in enumerate(row):
        # If the character is a digit, append to a rolling temp
        if ch.isdigit():
            temp["number"] += ch
            temp["positions"].append(ch_index)
        # If the character isn't a digit
        else:
            # But the temp contains a number, or rolling number shall I say
            if len(temp["positions"]) > 0:
                # Store the record for use later, and reset the rolling
                mapped_numbers.append(temp)
                temp = copy.deepcopy(template)
                temp["row"] = row_index

            # If the non-digit is a symbol we're looking for, append to the symbol map
            if any(substring in ch for substring in all_symbols):
                mapped_symbol.append(
                    {"row": row_index, "col": ch_index, "gear": ch == "*"}
                )

    # Catchall for a number at the end of a line
    if len(temp["positions"]) > 0:
        mapped_numbers.append(temp)

numbers_found = []
gears_with_two_adjacent_found = []
# Foreach symbol that we have
for symbol in mapped_symbol:
    possible = []

    # Find all the previous row numbers
    possible.extend(
        [item for item in mapped_numbers if item["row"] == symbol["row"] - 1]
    )
    # Find all this row numbers
    possible.extend([item for item in mapped_numbers if item["row"] == symbol["row"]])
    # Find all next row numbers
    possible.extend(
        [item for item in mapped_numbers if item["row"] == symbol["row"] + 1]
    )

    tmp = []
    # For all the possibilities
    for poss in possible:
        # If the possibility is left, centre, or right of the symbol, it's a part number
        if any(
            x in poss["positions"]
            for x in [symbol["col"] - 1, symbol["col"], symbol["col"] + 1]
        ):
            numbers_found.append(poss)

            # If it's a part number relating to a gear, append to a temp rolling again
            if symbol["gear"]:
                tmp.append(poss)

    # If the temp rolling only has 2, use for part two
    if len(tmp) == 2:
        gears_with_two_adjacent_found.append({"two": tmp})

print(f'Answer 1: {sum(list(map(lambda x: int(x["number"]), numbers_found)))}')

gear_total = 0
for i in gears_with_two_adjacent_found:
    gear_total += int(i["two"][0]["number"]) * int(i["two"][1]["number"])

print(f"Answer 2: {gear_total}")
