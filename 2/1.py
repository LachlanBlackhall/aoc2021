#!/usr/bin/python3
f = open('input')
mylist = []
for x in f.readlines():
    mylist.append(x.strip())
position = 0
depth = 0
for x in mylist:
    if (x.find("forward") != -1):
        position += int(x.split()[1])
    if (x.find("down") != -1):
        depth += int(x.split()[1])
    if (x.find("up") != -1):
        depth -= int(x.split()[1])
z = position * depth
print(z)
