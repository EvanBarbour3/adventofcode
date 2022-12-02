#!/usr/bin/env python3
import re

f = open('input.txt', 'r')

bingocalls = f.readline().strip().split(',')
f.readline()

bingocards = []
bingocards_won = []
temp_bingocard = []

# build cards
for x in f:
    if x.strip() == '':
        bingocards.append({'card': temp_bingocard, 'won': False})
        temp_bingocard = []
    elif '\n' not in x:
        line = re.sub("\s+", ",", x.strip()).split(',');
        temp_bingocard.append(line)
        bingocards.append({'card': temp_bingocard, 'won': False})
        temp_bingocard = []
    else:
        line = re.sub("\s+", ",", x.strip()).split(',');
        temp_bingocard.append(line)

for bingonumber in bingocalls:
    to_remove = []
    for cardindex in range(0, len(bingocards)): # go through each card
        if bingocards[cardindex]['won']:
            continue;

        for cardrowindex in range(0,5): # go down each row
            # print(cardindex, cardrowindex)
            if bingonumber in bingocards[cardindex]['card'][cardrowindex]: # dab card if contains called number
                bingocards[cardindex]['card'][cardrowindex][bingocards[cardindex]['card'][cardrowindex].index(bingonumber)] = None

        # check card for a bingo
        for columnindex in range(0,5): # go down each column too
            if all(xx is None for xx in bingocards[cardindex]['card'][columnindex]) or all(xx is None for xx in [el[columnindex] for el in bingocards[cardindex]['card']]):
                bingocards[cardindex]['won'] = True;
                bingocards[cardindex]['called'] = bingonumber;
                bingocards_won.append(
                    {
                        'card_number': cardindex,
                        'called_number': bingonumber,
                        'card_left': bingocards[cardindex]['card'],
                        'final_number': sum(list(map(int, filter(lambda final: final is not None, [item for sublist in bingocards[cardindex]['card'] for item in sublist])))) * int(bingonumber),
                    }
                )

                continue;

# Challenge 1
print('Answer 1: ' + str(bingocards_won[0]['final_number']))

# Challange 2
print('Answer 2: ' + str(bingocards_won[-1]['final_number']))
