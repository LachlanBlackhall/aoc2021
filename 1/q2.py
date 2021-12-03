#!/usr/bin/python3
f = open('input')
mylist = []
count=0
for x in f.readlines():
    mylist.append(int(x.strip()))
maxi = len(mylist)
i = 0
y = mylist[0] + mylist[1] + mylist[2]
while i < (maxi-2):
    x = mylist[i] + mylist[i+1] + mylist [i+2]
    if (x>y):
        count += 1
        print(str(x) + " > " + str(y))
    y = x
    i += 1
print("Q2 is " + str(count))
f.close()
