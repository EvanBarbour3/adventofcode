#!/usr/bin/env python3

f = open('input.txt', 'r')
ud = 0;
fb = 0;

for x in f:
    pos = x.split(' ')

    if pos[0] == 'up':
        ud = ud - int(pos[1])
    
    if pos[0] == 'down':
        ud = ud + int(pos[1])

    if pos[0] == 'forward':
        fb = fb + int(pos[1])
    
# Challenge 1
print('Answer 1: ' + str(ud * fb))

aim = 0
ud = 0;
fb = 0;

f.seek(0, 0)

for x in f:
    pos = x.split(' ')

    if pos[0] == 'up':
        aim = aim - int(pos[1])
    
    if pos[0] == 'down':
        aim = aim + int(pos[1])

    if pos[0] == 'forward':
        fb = fb + int(pos[1])
        ud = ud + (aim * int(pos[1]))
    
# Challenge 2
print('Answer 2: ' + str(ud * fb))
