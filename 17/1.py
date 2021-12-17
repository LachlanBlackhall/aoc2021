#!/usr/bin/python3
#c_input = 'target area: x=20..30 y=-10..-5'
c_input = 'target area: x=119..176 y=-141..-84'
input_x = c_input.split(' ')[2].split('=')[1].split('..')
input_y = c_input.split(' ')[3].split('=')[1].split('..')

print(f'{input_x} and {input_y}')


def next_coord(x, y, x_vel, y_vel):
    x += x_vel
    y += y_vel
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1
    y_vel -= 1
    # print(f'Next coords are {x}, {y} with vels {x_vel},{y_vel}')
    return [x, y, x_vel, y_vel]

x_vels = []
y_vels = []
neg_y_vels = []
landed_vels = []
highest_y = 0

for i in range(0,300):
    x_vels.append(i)
for i in range(0,300):
    y_vels.append(i)
for i in range(0,-300,-1):
    neg_y_vels.append(i)

for x_vel in x_vels:
    for y_vel in y_vels:
        landed = False
        print(f'Starting with {x_vel},{y_vel}')
        start_x_vel = x_vel
        start_y_vel = y_vel
        cur_y_vel = y_vel
        cur_x_vel = x_vel
        cur_x, cur_y, cur_x_vel, cur_y_vel = next_coord(0, 0, cur_x_vel, cur_y_vel)
        max_y = cur_y
        while not landed:
            if cur_y > max_y:
                max_y = cur_y
            if cur_x >= int(input_x[0]) and cur_x <= int(input_x[1]) and cur_y <= int(input_y[1]) and cur_y >= int(input_y[0]):
                print(f'At {cur_x}, {cur_y}')
                if max_y > highest_y:
                    if [start_x_vel, start_y_vel] not in landed_vels:
                        landed_vels.append([start_x_vel, start_y_vel])
                    highest_y = max_y
                else:
                    if [start_x_vel, start_y_vel] not in landed_vels:
                        landed_vels.append([start_x_vel, start_y_vel])
                landed = True
            if cur_x > int(input_x[1]) or cur_y < int(input_y[0]):
                landed = True
            cur_x, cur_y, cur_x_vel, cur_y_vel = next_coord(cur_x, cur_y, cur_x_vel, cur_y_vel)

for x_vel in x_vels:
    for y_vel in neg_y_vels:
        landed = False
        print(f'Starting with {x_vel},{y_vel}')
        start_x_vel = x_vel
        start_y_vel = y_vel
        cur_y_vel = y_vel
        cur_x_vel = x_vel
        cur_x, cur_y, cur_x_vel, cur_y_vel = next_coord(0, 0, cur_x_vel, cur_y_vel)
        max_y = cur_y
        while not landed:
            if cur_y > max_y:
                max_y = cur_y
            if cur_x >= int(input_x[0]) and cur_x <= int(input_x[1]) and cur_y <= int(input_y[1]) and cur_y >= int(input_y[0]):
                print(f'At {cur_x}, {cur_y}')
                if max_y > highest_y:
                    if [start_x_vel, start_y_vel] not in landed_vels:
                        landed_vels.append([start_x_vel, start_y_vel])
                    highest_y = max_y
                else:
                    if [start_x_vel, start_y_vel] not in landed_vels:
                        landed_vels.append([start_x_vel, start_y_vel])
                landed = True

            if cur_x > int(input_x[1]) or cur_y < int(input_y[0]):
                print(f'Ended on {cur_x}, {cur_y}')
                landed = True
            cur_x, cur_y, cur_x_vel, cur_y_vel = next_coord(cur_x, cur_y, cur_x_vel, cur_y_vel)
print(f'sorted vels is {sorted(landed_vels)}')
print(f'With vel {len(landed_vels)} I got to {highest_y}')

            

    


