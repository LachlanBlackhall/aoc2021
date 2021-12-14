#!/usr/bin/python3
import collections, re, pdb


def return_zero():
    return 0


# f = open('test').read().splitlines()
f = open('input').read().splitlines()
insertions = []
template = f[0]
count = collections.defaultdict(return_zero)

for i in range(2,len(f)):
    insertions.append(f[i])

for i in range(0, 40):
    progress_polymer = ''
    changes = []
    
    for chari, char in enumerate(template):
        for change in insertions:
            if chari != len(template)-1:
                if char + template[chari+1] == change.split(' ')[0]:
                    changes.append([chari, change.split(' ')[2]])
    for z, char in enumerate(template):
        progress_polymer += char
        for change in changes:
            if change[0] == z:
                progress_polymer += change[1]
    template = progress_polymer

for char in template:
    count[char] += 1

maxx = 0
minn = 999999999999999999999999
maxchar = ''
minchar = ''
for char in count:
    print(f'{char} with {count[char]}')
    if count[char] > maxx:
        maxx = count[char]
        maxchar = char
    elif count[char] < minn:
        minn = count[char]
        minchar = char
print(f'I think max is {maxx} {maxchar} and min is {minn} {minchar}')
print(int(maxx) - int(minn))
