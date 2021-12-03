#!/usr/bin/python3
f = open('input')
mylist = []
count=0
for x in f.readlines():
    mylist.append(int(x.strip()))
y = mylist[0]
for x in mylist:
    if (x>y):
        count += 1
        print(str(x) + " > " + str(y))
    y = x
print("Q1 is " + str(count))
f.close()
