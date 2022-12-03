#!/usr/bin/env python3

f = open('input.txt', 'r')

def challenge(f, days_to_run: int = 80):
    lanternfishlist = list(map(int, f.readline().split(',')))
    lanternfish = [0] * 9;

    for current in lanternfishlist:
        lanternfish[current] += 1

    for i in range(0, days_to_run):
        zero = 0
        for lf in range(0, len(lanternfish)):
            if lf == 0:
                zero = lanternfish[0]
                lanternfish[0] = 0
            else:
                lanternfish[lf-1] = lanternfish[lf]
        
        lanternfish[6] += zero
        lanternfish[8] = zero

    return sum(lanternfish)

print('Answer 1: ' + str(challenge(f)))
f.seek(0,0)
print('Answer 2: ' + str(challenge(f, 256)))
