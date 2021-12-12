#!/usr/bin/python3
import time, pdb, traceback

# f = open('test').read().splitlines()
f = open('input').read().splitlines()
split_list = [[99999]]
queue = []
flash_count = 0


def flash(flashed, flash_count, queue, x, y, car):
    flashed.append(f'{x};{y}')
    flash_count += 1
    queue.append(f'{x};{y}')
    # print(f'Added {x};{y} to queue from direction {car}')
    return flashed, flash_count, queue

for i in range(0,11):
    split_list[0].append(99999)
for i, line in enumerate(f):
    split_list.append([99999])
    for num_char in line:
        split_list[i+1].append(int(num_char))
    split_list[i+1].append(99999)
split_list.append([99999])
for i in range(0,11):
    split_list[len(split_list)-1].append(99999)

for i in range(0,100):
    copy_list = split_list.copy()
    flashed = []
    for y, line in enumerate(split_list):
        for x, num in enumerate(line):
            # print(f'Checking {num} at {x};{y}')
            if num == 99999:
                continue
            if int(copy_list[y][x]) >= 9 and f'{x};{y}' not in flashed: 
                flashed, flash_count, queue = flash(flashed, flash_count, queue, x, y, 'O')
                while queue:
                    try:
                        # print(f'Pre pop queue is {queue}')
                        s_x, s_y = (int(i) for i in queue.pop().split(';'))
                        # print(f'S-coords are {s_x};{s_y}')
                        # print(f'Post pop queue is {queue}')
                        # pdb.set_trace()
                        if copy_list[s_y][s_x] == 99999:
                            continue
                        if int(copy_list[s_y-1][s_x-1]) >= 9 and f'{s_x-1};{s_y-1}' not in flashed and int(copy_list[s_y-1][s_x-1]) != 99999:
                            flashed, flash_count, queue = flash(flashed, flash_count, queue, s_x-1, s_y-1, 'NW')
                        elif int(copy_list[s_y-1][s_x-1]) != 99999:
                            copy_list[s_y-1][s_x-1] += 1
                        if int(copy_list[s_y-1][s_x]) >= 9 and f'{s_x};{s_y-1}' not in flashed and int(copy_list[s_y-1][s_x]) != 99999:
                            flashed, flash_count, queue = flash(flashed, flash_count, queue, s_x, s_y-1, 'N')
                        elif int(copy_list[s_y-1][s_x]) != 99999:
                            copy_list[s_y-1][s_x] += 1
                        if int(copy_list[s_y-1][s_x+1]) >= 9 and f'{s_x+1};{s_y-1}' not in flashed and int(copy_list[s_y-1][s_x+1]) != 99999:
                            flashed, flash_count, queue = flash(flashed, flash_count, queue, s_x+1, s_y-1, 'NE')
                        elif int(copy_list[s_y-1][s_x+1]) != 99999:
                            copy_list[s_y-1][s_x+1] += 1
                        if int(copy_list[s_y][s_x-1]) >= 9 and f'{s_x-1};{s_y}' not in flashed and int(copy_list[s_y][s_x-1]) != 99999:
                            flashed, flash_count, queue = flash(flashed, flash_count, queue, s_x-1, s_y, 'E')
                        elif int(copy_list[s_y][s_x-1]) != 99999:
                            copy_list[s_y][s_x-1] += 1
                        if int(copy_list[s_y][s_x+1]) >= 9 and f'{s_x+1};{s_y}' not in flashed and int(copy_list[s_y][s_x+1]) != 99999:
                            flashed, flash_count, queue = flash(flashed, flash_count, queue, s_x+1, s_y, 'W')
                        elif int(copy_list[s_y][s_x+1]) != 99999:
                            copy_list[s_y][s_x+1] += 1
                        if int(copy_list[s_y+1][s_x-1]) >= 9 and f'{s_x-1};{s_y+1}' not in flashed and int(copy_list[s_y+1][s_x-1]) != 99999:
                            flashed, flash_count, queue = flash(flashed, flash_count, queue, s_x-1, s_y+1, 'SW')
                        elif int(copy_list[s_y+1][s_x-1]) != 99999:
                            copy_list[s_y+1][s_x-1] += 1
                        if int(copy_list[s_y+1][s_x]) >= 9 and f'{s_x};{s_y+1}' not in flashed and int(copy_list[s_y+1][s_x]) != 99999:
                            flashed, flash_count, queue = flash(flashed, flash_count, queue, s_x, s_y+1, 'S')
                        elif int(copy_list[s_y+1][s_x]) != 99999:
                            copy_list[s_y+1][s_x] += 1
                        if int(copy_list[s_y+1][s_x+1]) >= 9 and f'{s_x+1};{s_y+1}' not in flashed and int(copy_list[s_y+1][s_x+1]) != 99999:
                            flashed, flash_count, queue = flash(flashed, flash_count, queue, s_x+1, s_y+1, 'SE')
                        elif int(copy_list[s_y+1][s_x+1]) != 99999:
                            copy_list[s_y+1][s_x+1] += 1                 
                    except Exception as e:
                        # print(e)
                        # print(traceback.format_exc())
                        pdb.set_trace()
            else:   
                copy_list[y][x] += 1
    for y, line in enumerate(split_list):
        for x, num in enumerate(line):
            if f'{x};{y}' in flashed:
                copy_list[y][x] = 0
    split_list = copy_list.copy()

print(flash_count)
                
            
            

