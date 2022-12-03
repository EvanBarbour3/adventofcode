#!/usr/bin/env python3

f = open('input.txt', 'r')

def challenge(f, rundiagonals: bool = False):
    coords = []
    diagram = []

    # list coordinates
    for line in f:
        coords.append(','.join(line.strip().split(' -> ')).split(','))

    # get map max
    mapmax = max(map(int, [item for sublist in coords for item in sublist])) + 1

    # build the diagram / hydrothermal map
    for i in range(0, mapmax):
        diagram.append([0] * mapmax)

    for coord in coords:
        if (coord[1] == coord[3]): # horizontal
            temprange = [int(coord[0]), int(coord[2])];
            temprange.sort()
            temprange[1] += 1

            for i in range(temprange[0], temprange[1]):
                diagram[int(coord[1])][i] += 1;
        
        elif (coord[0] == coord[2]): # vertical
            temprange = [int(coord[1]), int(coord[3])];
            temprange.sort()
            temprange[1] += 1
 
            for i in range(temprange[0], temprange[1]):
                diagram[i][int(coord[0])] += 1;

        elif rundiagonals: # diagonals
            temprange1 = [int(coord[0]), int(coord[2])];
            temprange1increment = 1
            if temprange1[0] > temprange1[1]:
                temprange1[1] -= 1
                temprange1increment = -1
            else:
                temprange1[1] += 1

            temprange2 = [int(coord[1]), int(coord[3])];
            temprange2increment = 1
            if temprange2[0] > temprange2[1]:
                temprange2[1] -= 1
                temprange2increment = -1
            else:
                temprange2[1] += 1

            range1 = [*range(temprange1[0], temprange1[1], temprange1increment)]
            range2 = [*range(temprange2[0], temprange2[1], temprange2increment)]

            for i in range(0, len(range1)):
                diagram[range2[i]][range1[i]] += 1
 
    # Pretty print
    # for d in diagram:
    #     print(''.join(map(str, map(lambda x: x if x > 0 else '.', d))))

    return len(list(map(int, filter(lambda final: final > 1, [item for sublist in diagram for item in sublist]))))

print('Answer 1: ' + str(challenge(f)))
f.seek(0,0)
print('Answer 2: ' + str(challenge(f, True)))
