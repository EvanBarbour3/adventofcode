#!/usr/bin/env python3

f = open('input.txt', 'r')

def fetch_item_in_both_compartments(str1: str, str2: str):
    res = ''
    for i in str1:
        if i in str2 and not i in res:
            res += i

    return res

def item_to_priority(item: str):
    if item.isupper():
        return ord(item) - 64 + 26
    
    return ord(item) - 96

def challenge1(f):
    priorities = []

    for i in f:
        str1 = i[:len(i)//2]
        str2 = i[len(i)//2:]

        item = fetch_item_in_both_compartments(str1, str2)
        priorities.append(item_to_priority(item))

    # Challenge 1
    print('Answer 1: ' + str(sum(priorities)))
    
def challenge2(f):
    priorities = []

    counter = 0;
    group = []
    for i in f:
        counter += 1

        group.append(i)
        if counter % 3 == 0:
            item = fetch_item_in_both_compartments(
                fetch_item_in_both_compartments(
                    group[0],
                    group[1]
                ),
                group[2]
            )
            
            priorities.append(item_to_priority(item.strip()))
            group = []
        
    # Challenge 2
    print('Answer 2: ' + str(sum(priorities)))

challenge1(f)
f.seek(0,0)
challenge2(f)
