#!/usr/bin/python3
import re
import pandas as pd
import numpy as np

f = open('input').read().splitlines()
coordpairs = []
maxx = maxy = danger = 0

# Get the coordinate pairs from the file without the ->
for line in f:
    coordpairs.append(re.findall('(\d+,\d+)', line))

# Get the grid dimensions
for coords in coordpairs:
    for coord in coords:
        if int(coord.split(',')[0]) > maxx: maxx = int(coord.split(',')[0])
        if int(coord.split(',')[1]) > maxy: maxy = int(coord.split(',')[1])
print(f'Max x is {maxx} and max y is {maxy}')

# Create the grid with int zeroes
df = pd.DataFrame(np.zeros((maxx+1, maxy+1))).astype('int64')

for coords in coordpairs:
    # Split coordinates up and cast to int
    x1 = int(coords[0].split(',')[0])
    y1 = int(coords[0].split(',')[1])
    x2 = int(coords[1].split(',')[0])
    y2 = int(coords[1].split(',')[1])
    # Handle horizontal and vertical lines first
    if x1 == x2 or y1 == y2:
        # Create horizontal lines
        if x1 < x2:
            for i in range(x1, x2+1): # Use inclusive range
                df.iat[y1, i]+=1 # Pandas uses y,x not x,y
        elif x1 > x2:
            for i in range(x2, x1+1):
                df.iat[y1, i]+=1
        # Create vertical lines
        if y1 < y2:
            for i in range(y1, y2+1):
                df.iat[i, x1]+=1
        elif y1 > y2:   
            for i in range(y2, y1+1):
                df.iat[i, int(coords[0].split(',')[0])]+=1

    # Handle diagonal lines next
    if x1 != x2 and y1 != y2:
        if x1 < x2: 
            counter = 0
            for i in range(x1, x2+1):
                if y1 > y2: # 0,8 -> 8,0
                    df.iat[y1-counter, i]+=1 # 0,8 -> 1,7 -> 2,6 etc.
                    counter+=1
                elif y1 < y2: # 0,0 -> 8,8
                    df.iat[y1+counter, i]+=1 # 0,0 -> 1,1 -> 2,2 etc.
                    counter+=1
        elif x2 < x1:
            counter = 0
            for i in range(x2, x1+1):
                if y1 > y2: # 8,8 -> 0,0
                    df.iat[y2+counter, i]+=1 # 0,0 -> 1,1 -> 2,2 etc.
                    counter+=1
                elif y1 < y2: #8,0 -> 0,8
                    df.iat[y2-counter, i]+=1 # 0,8 -> 1,7 -> 2,6 etc.
                    counter+=1

# Check each cell in the DataFrame for crossovers
for x in range(0, maxx+1):
    for y in range(0, maxy+1):
        if df.iat[y, x] >= 2:
            danger+=1

print(f'There are {danger} dangerous spots')
