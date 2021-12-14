#!/usr/bin/python3
import numpy as np
import pandas as pd

f = open('input').read().splitlines()

folds = []
coords = []

for line in f:
    if not line:
        pass
    elif line[0] == 'f':
        folds.append(line.split(' ')[-1])
    else:
        coords.append(line.split(','))

for fold in folds:
    folded_coords = []
    for coord_pair in coords:
        fold_pair = fold.split('=')
        if fold_pair[0] == 'x':
            if int(coord_pair[0]) > int(fold_pair[1]):
                diff = (int(coord_pair[0]) - int(fold_pair[1])) * 2
                if [int(coord_pair[0]) - diff, int(coord_pair[1])] not in folded_coords:
                    folded_coords.append([int(coord_pair[0]) - diff, int(coord_pair[1])])
            else:
                if [int(coord_pair[0]), int(coord_pair[1])] not in folded_coords:
                    folded_coords.append([int(coord_pair[0]), int(coord_pair[1])])
        if fold_pair[0] == 'y':
            if int(coord_pair[1]) > int(fold_pair[1]):
                diff = (int(coord_pair[1]) - int(fold_pair[1])) * 2
                if [int(coord_pair[0]), int(coord_pair[1]) - diff] not in folded_coords:
                    folded_coords.append([int(coord_pair[0]), int(coord_pair[1]) - diff])
            else:
                if [int(coord_pair[0]), int(coord_pair[1])] not in folded_coords:
                    folded_coords.append([int(coord_pair[0]), int(coord_pair[1])])
    if folded_coords: 
        coords = folded_coords.copy()

zero_data = np.zeros(shape=(7, 40))
d = pd.DataFrame(zero_data).astype('object')

for i in range(0,40):
    for x in range(0,7):
        d.at[x, i] = '.'

for coord in coords:
    d.at[coord[1], coord[0]] = '@'
pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", 1000)
print(d)
