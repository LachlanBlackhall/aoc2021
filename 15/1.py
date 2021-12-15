#!/usr/bin/python3


def get_neighbors(f, coords):
    x = coords[0]
    y = coords[1]
    neighbors = []
    if f[y-1][x] != 'A':
        neighbors.append([x, y-1])
    if f[y][x+1] != 'A':
        neighbors.append([x+1, y])
    if f[y+1][x] != 'A':
        neighbors.append([x, y+1])
    if f[y][x-1] != 'A':
        neighbors.append([x-1, y])
    # print(f'Neigh is {neighbors}')
    return neighbors


f = open('test').read().splitlines()
buffered = ['']
for i in range(0, len(f[0])+2):
    buffered[0] += 'A'

for i in range(1, len(f)):
    buffered.append('A')
    buffered[i] += f[i-1]
    buffered[i] += 'A'

tempstr = ''
for i in range(0, len(buffered[0])):
    tempstr += 'A'

buffered.append(tempstr)
split_list = []
starting = [1, 1]
ending = [len(buffered[0])-2, len(buffered)-2]
inpr_paths = [[starting]]
finished_paths = []
danger = 999999999999999999999999999
next_inpr_paths = []

while inpr_paths:
    path = inpr_paths.pop()
    possible_paths = [path]
    for i in range(0,3):
        temp_paths = []
        while possible_paths:
            next_path = possible_paths.pop()
            print(next_path)
            for neighbor in get_neighbors(buffered, next_path[-1]):
                new_path = next_path.copy()
                new_path.append(neighbor)
                if neighbor == ending:
                    finished_paths.append(new_path)
                else:
                    temp_paths.append(new_path)
        possible_paths = temp_paths.copy()
    current_min = 999999999999999999999999999
    for path in possible_paths:
        tempcount2 = 0
        for coord in path:
            tempcount2 += int(buffered[coord[1]][coord[0]])
        if tempcount2 < current_min:
            next_inpr_paths = path.copy()
    if next_inpr_paths:
        inpr_paths = next_inpr_paths.copy()
        print(inpr_paths)

for path in finished_paths:
    tempcounter = 0
    for coord in path:
        tempcounter += int(buffered[coord[1]][coord[0]])
    if tempcounter < danger:
        danger = tempcounter
        finished_path = path

       #  for neighbor in get_neighbors(buffered, path[-1]):
       #      new_path = path.copy()
       #      new_path.append(neighbor)
       #      if neighbor not in path:
       #          count = 0
       #          if neighbor == ending:
       #              new_path.append(ending)
       #              for coord in new_path[1:]:
       #                  count += int(buffered[coord[1]][coord[0]])
       #              if count < danger:
       #                  finished_path = new_path
       #                  danger = count
       #                  
       #          else:
       #              for coord in new_path:
       #                  count += int(buffered[coord[1]][coord[0]])
       #              if count <= danger:
       #                  inpr_paths.append(new_path)

print(danger)
