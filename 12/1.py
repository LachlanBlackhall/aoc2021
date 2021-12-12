#!/usr/bin/python3
import collections, re


def return_zero():
    return 0

# f = open('test').read().splitlines()
f = open('input').read().splitlines()

struc = collections.defaultdict(return_zero)
inpr_paths = []
finished_paths = []
finished = False

for line in f:
    r1 = line.split('-')[0]
    r2 = line.split('-')[1]
    if r1 in struc and r2 not in struc[r1]:
        struc[r1].append(r2)
    elif r1 not in struc:
        struc[r1] = [r2]
    if r2 in struc and r1 not in struc[r2]:
        struc[r2].append(r1)
    elif r2 not in struc:
        struc[r2] = [r1]

for room in struc['start']:
    inpr_paths.append(f'start,{room}')


while inpr_paths:
    path = inpr_paths.pop()
    for room in struc[path.split(',')[-1]]:
        if room == 'end':
            finished_paths.append(path + ',end')
        elif room.isupper():
           inpr_paths.append(path + ',' + room)
        elif room not in path and room.islower():
            inpr_paths.append(path + ',' + room)
        

# print(finished_paths)
print(len(finished_paths))
    
