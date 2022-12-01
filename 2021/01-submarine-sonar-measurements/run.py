#!/usr/bin/env python3

f = open('input.txt', 'r')
d = []

previous = 0
times = -1
for x in f:
    if int(x) > previous:
        times = times+1
    previous = int(x)

    # For challenge 2
    d.append(int(x))

# Challenge 1
print('Answer 1: ' + str(times))

i = 0;
previous = sum(d[0:3])
answer = 0
for x in range(1, len(d)):
    # print(x+1)
    new = sum(d[x:x+3])
    if new > previous:
        answer = answer + 1
    previous = new
    i = i+1

# Challenge 2
print('Answer 2: ' + str(answer))
