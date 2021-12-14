#!/usr/bin/python3

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
    break

print(len(coords))
