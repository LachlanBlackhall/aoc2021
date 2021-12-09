#!/usr/bin/python3

def check_cardinals(char, north, east, south, west):
    if int(char) >= int(north):
        return False
    if int(char) >= int(east):
        return False
    if int(char) >= int(south):
        return False
    if int(char) >= int(west):
        return False
    return True


# This function starts with a single danger point
# It then iteratively checks each cardinal point around it
# until it finds the complete size of the basin
# The if statements check if the next cardinal point is bigger
# then the current one as well as making sure the next point
# isn't a 9 (max height) and that the point hasn't already 
# being queued or visited
def check_basin(coords, split_list):
    queue = [coords]
    visited = []
    size = 0
    while queue: 
        x, y = [int(i) for i in queue.pop()]
        visited.append(f'{x};{y}')
        size+=1
        char = split_list[y][x]
        north = split_list[y-1][x]
        east = split_list[y][x+1]
        south = split_list[y+1][x]
        west = split_list[y][x-1]
        if (int(char) < int(north) and north != '9' 
            and f'{x};{y-1}' not in visited and [x, y-1] not in queue):
            queue.append([x, y-1])
        if (int(char) < int(east) and east != '9' 
            and f'{x+1};{y}' not in visited and [x+1, y] not in queue):
            queue.append([x+1, y])
        if (int(char) < int(south) and south != '9' 
            and f'{x};{y+1}' not in visited and [x, y+1] not in queue):
            queue.append([x, y+1])
        if (int(char) < int(west) and west != '9' 
            and f'{x-1};{y}' not in visited and [x-1, y] not in queue):
            queue.append([x-1, y])
    return size
        
    
# Start by adding a wall of 9's aroun the input
# This will prevent index issues later
f = open('input').read().splitlines()
split_list = ['9']
for i in range(0, len(f[0])+1):
    split_list[0] += '9'
final_count = 0
for i, line in enumerate(f):
    split_list.append('9')
    for char in line:
        split_list[i+1] += char 
    split_list[i+1] += '9'
split_list.append('9')
for i in range(0, len(f[0])+1):
    split_list[len(split_list)-1] += '9'

basins = []
for y, line in enumerate(split_list):
    if y == 0 or y == (len(split_list)-1): continue
    for x, char in enumerate(line):
        if x == 0 or x == (len(line)-1) or char == '9': continue
        # Check the four cardinal directions        
        if check_cardinals(char, split_list[y-1][x], split_list[y][x+1],
                                 split_list[y+1][x], split_list[y][x-1]):
            basins.append(check_basin([x,y], split_list))
basins = sorted(basins, reverse=True)
print(basins[0] * basins[1] * basins[2])
