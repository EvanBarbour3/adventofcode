#!/usr/bin/env python3

f = open('input.txt', 'r')

def challenge1(f):
    digits = len(f.readline())-1
    f.seek(0,0)

    lines = len(f.readlines())
    f.seek(0,0)    

    gamma = []
    epsilon = []

    for i in range(0, digits):

        ones = 0;
        zeros = 0;

        for x in f:
        
            if x[i] == '1':
                ones = ones + 1
            else:
                zeros = zeros + 1
            
        f.seek(0,0)

        if ones > zeros:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')

    # Challenge 1
    print('Answer 1: ' + str(int(''.join(gamma), 2) * int(''.join(epsilon), 2)))

def challenge2(f):
    # Challenge 1
    f.seek(0,0)
    oxygen = __c2wrap(f, 'oxygen')
    f.seek(0,0)
    co2 = __c2wrap(f, 'co2')
    print('Answer 2: ' + str(oxygen * co2))


def __c2wrap(f, type: str):
    f.seek(0,0)
    digits = len(f.readline())-1
    f.seek(0,0)

    member = []
    memberchoose = 0;

    for x in f:
        member.append(x)
    f.seek(0,0)

    for i in range(0, digits):
        ones = 0;
        zeros = 0;

        for x in range(len(member)):
            if member[x][i] == '1':
                ones = ones + 1
            else:
                zeros = zeros + 1

        if type == 'oxygen':
            if ones >= zeros:
                memberchoose = '1';
            else:
                memberchoose = '0';
        else:
            if zeros <= ones:
                memberchoose = '0';
            else:
                memberchoose = '1';

        member = __c2strip(member, i, memberchoose)

        if len(member) == 1:
            return int(''.join(member), 2)
            # break

def __c2strip(data: list, pos: int, choose: str):
    ones = 0;
    zeros = 0;

    rtn = []

    for x in data:
        if x[pos] == choose:
            rtn.append(x)

    return rtn

challenge1(f)
challenge2(f)

