#!/usr/bin/python3
epsilonl = gammal = open('input').read().splitlines()
i=0
while len(gammal) > 1:
    counter = [0,0]
    for line in gammal:
        if line[i] == '0':
            counter[0]+=1
        else:
            counter[1]+=1
    cpl = []
    for line in gammal:
        if counter[1] >= counter[0]:
            if line[i] == '1': cpl.append(line)
        else:
            if line[i] == '0': cpl.append(line)
    gammal = cpl
    i+=1
oxygen = int(gammal[0], 2)
i=0
while len(epsilonl) > 1:
    counter = [0,0]
    for line in epsilonl:
        if line[i] == '0':
            counter[0]+=1
        else:
            counter[1]+=1
    cpl = []
    for line in epsilonl:
        if counter[0] <= counter[1]:
            if line[i] == '0': cpl.append(line)
        else:
            if line[i] == '1': cpl.append(line)
    epsilonl = cpl
    i+=1
co2 = int(epsilonl[0], 2)
print(oxygen*co2)
