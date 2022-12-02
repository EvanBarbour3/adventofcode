#!/usr/bin/env python3

f = open('input.txt', 'r')

def challenges(f):
    round1 = 0
    round2 = 0

    for x in f:
        decisions = x.strip().split(' ')

        resultdict = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
        expectedresultdict = {'X': 1, 'Y': 0, 'Z': 2}
        shapesdict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
        winner1 = (3 + resultdict[decisions[0]] - resultdict[decisions[1]]) % 3;
        result1 = 0 if winner1 == 1 else 6 if winner1 == 2 else 3
        round1 += result1 + shapesdict[decisions[1]]

        pt2expected = expectedresultdict[decisions[1]]
        for i in ['X', 'Y', 'Z']:
            winner2 = (3 + resultdict[decisions[0]] - resultdict[i]) % 3;
            if winner2 == pt2expected:
                result2 = 0 if winner2 == 1 else 6 if winner2 == 2 else 3
                round2 += result2 + shapesdict[i]

    # Challenge 1
    print('Answer 1: ' + str(round1))

    # Challenge 2
    print('Answer 2: ' + str(round2))

challenges(f)
