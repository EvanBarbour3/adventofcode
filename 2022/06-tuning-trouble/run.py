#!/usr/bin/env python3
import re

f = open('input.txt', 'r')

def challenge(f, take_amount: int = 4):
    s = list(f.readline())
    complete = 0
    prev = []
    for i in s:
        complete += 1
        prev.append(i)

        if len(list(set(prev[-take_amount:]))) == take_amount:
            return complete
        
    return complete


    # return final

print('Answer 1: ' + str(challenge(f)))
f.seek(0,0)
print('Answer 2: ' + str(challenge(f, 14)))
