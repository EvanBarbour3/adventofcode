#!/usr/bin/env python3

f = open('input.txt', 'r')
i = 0
d = []

for x in f:
    if x in ['\n', '\r\n']:
        i = i+1
    else:
        if len(d) == i:
            d.append(int(x))
        else:
            d[i] = d[i] + int(x)

d.sort(reverse=True)

# Challenge 1
print('The elf carrying the most calories: ' + str(d[0]))

# Challenge 2
print('The 3 elves carrying the most calories: ' + str(sum(d[0:3])))
