#!/usr/bin/python3

f = open('input').read().splitlines()
#f = open('input').read().splitlines()
# f = open('test').read().splitlines()

myl=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
gamma = []
other = []

for line in f:
    for i, ch in enumerate(line):
        if ch == '0':
            myl[i][0]+=1
        else:
            myl[i][1]+=1
for i in myl:
    if i[0] > i[1]: 
        gamma.append('0')
        other.append('1')
    else:
        other.append('0')
        gamma.append('1')
print(gamma)
print(other)
print(int(''.join(gamma), 2) * int(''.join(other), 2))


