#!/usr/bin/python3
f = open('input').read().splitlines()
crabs = []
min_fuel = 0
for line in f:
    for crab in line.split(','):
        crabs.append(crab)

def fuel_cost(steps):
    cost = 0
    for i in range(0,steps+1):
        cost+= i
    return cost

first_run = True
for i in range(int(min(crabs)), int(max(crabs))+1):
    current_fuel = 0
    for crab in crabs:
        if first_run:
            min_fuel+= fuel_cost(max([int(crab), i]) - min([int(crab), i]))
        else:
            current_fuel+= fuel_cost(max([int(crab), i]) - min([int(crab), i]))
    if current_fuel < min_fuel and not first_run: min_fuel = current_fuel
    first_run = False

print(min_fuel)

