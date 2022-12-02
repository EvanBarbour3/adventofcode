#!/usr/bin/env python3

f = open('input.txt', 'r')

def challenges(f):
    round1 = 0
    round2 = 0

    for x in f:
        decisions = x.strip().split(' ')
        answer = decide(decisions[0], decisions[1])
        
        round1 += answer[0]
        round2 += answer[1]

    # Challenge 1
    print('Answer 1: ' + str(round1))

    # Challenge 2
    print('Answer 2: ' + str(round2))

def decide(them: str, you: str):
    round1 = 0
    round2 = 0

    match them:
        case 'A': # rock
            if you == 'X': # rock, lose
                round1 += 3 + 1
                round2 += 0 + 3
            if you == 'Y': # paper, draw
                round1 += 6 + 2
                round2 += 3 + 1
            if you == 'Z': # scissors, win
                round1 += 0 + 3
                round2 += 6 + 2
        case 'B': # paper
            if you == 'X':
                round1 += 0 + 1
                round2 += 0 + 1
            if you == 'Y':
                round1 += 3 + 2
                round2 += 3 + 2
            if you == 'Z':
                round1 += 6 + 3
                round2 += 6 + 3
        case 'C': # scissors
            if you == 'X':
                round1 += 6 + 1
                round2 += 0 + 2
            if you == 'Y':
                round1 += 0 + 2
                round2 += 3 + 3
            if you == 'Z':
                round1 += 3 + 3
                round2 += 6 + 1

    return (round1, round2)

challenges(f)