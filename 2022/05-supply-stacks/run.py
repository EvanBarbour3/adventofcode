#!/usr/bin/env python3
import re

f = open('input.txt', 'r')

def challenge(f, take_single: bool = True):
    raw_stacks = []
    found_end_of_stack = False
    # i = 0

    # Figure out the amount of stacks
    while not found_end_of_stack:
        line = f.readline()

        if line.strip() == '':
            found_end_of_stack = True
        else:
            raw_stacks.append(line)

    max_stack = max(map(int, list(raw_stacks.pop().strip().replace(' ', ''))))
    reg = ' '.join((['(.{0,3})'] * max_stack))

    # Build stacks
    stacks = {} 
    while not len(raw_stacks) == 0:
        line = raw_stacks.pop()
        # print('checking line', line, re.match(reg, line).groups())
        matches = [*map(lambda x: x.replace('[', '').replace(']', ''), re.match(reg, line).groups())]

        for i in range(0, len(matches)):
            if i not in stacks:
                stacks[i] = [matches[i]]
            else:
                if not len(matches[i].strip()) == 0:
                    stacks[i].append(matches[i])

    # Move stacks
    instruction_reg = 'move (.*?) from (.*?) to (.*)'
    for line in f:
        instruction = [*map(int, re.match(instruction_reg, line).groups())]
        to_move = stacks[instruction[1]-1][-instruction[0]:]

        if take_single:
            while len(to_move) > 0:
                stacks[instruction[2]-1].append(to_move.pop())
                stacks[instruction[1]-1].pop()
        else:
            stacks[instruction[2]-1].extend(to_move)
            while len(to_move) > 0:
                to_move.pop()
                stacks[instruction[1]-1].pop()

    final = ''
    for i in stacks:
        final = final + stacks[i][-1]

    return final

print('Answer 1: ' + str(challenge(f)))
f.seek(0,0)
print('Answer 2: ' + str(challenge(f, False)))
