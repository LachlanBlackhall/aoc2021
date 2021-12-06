#!/usr/bin/python3
from collections import defaultdict
f = open('input').read().splitlines()
def return_zero():
    return 0
fishes = defaultdict(return_zero)
numfish=0
for line in f:
    for fish in line.split(','):
        fishes[fish]+=1
for i in range(0,80):
    fishes2 = defaultdict(return_zero)
    for x in range(0, 9):
        if x == 0:
            fishes2['8']+=fishes['0']
            fishes2['6']+=fishes['0']
        else:
            fishes2[str(x-1)]+=fishes[str(x)]
    fishes = fishes2
for z in range(0,9):
    numfish+=fishes[str(z)]
print(numfish)
