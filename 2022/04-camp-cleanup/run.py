#!/usr/bin/env python3

f = open('input.txt', 'r')

count1 = 0
count2 = 0

for line in f:
    split_up = [*map(int, ','.join(line.strip().split('-')).split(','))]
    count1 += int(split_up[0] <= split_up[2] <= split_up[3] <= split_up[1] or split_up[2] <= split_up[0] <= split_up[1] <= split_up[3])
    count2 += int(min(split_up[1], split_up[3]) >= max(split_up[0], split_up[2]))

# Challenge 1
print('Answer 1: ' + str(count1))

f.seek(0,0)
count = 0

# Challenge 2
print('Answer 1: ' + str(count2))
