#!/usr/bin/python3
def check_hor_board(board):
    win = False
    for line in board:
        for num in line:
            if num[-1] != 'Y':
                win = False
                break
            else: 
                win = True
        if win:
            print('Horizontal win')
            return True
    return False

def check_ver_board(board):
    win = False
    for hor in range(0,4):
        for ver in range(0,4):
            if board[ver][hor][-1] == 'Y':
                win = True
            else:
                win = False
                break
        if win:
            print('Vertical win')
            return True
    return False

f = open('input').read().splitlines()
numbers = f[0].split(',')
boards = [[]]
i = winsum = 0
for line in f[2:]:
    if line != '':
        boards[i].append(line.split())
    else:
        boards.append([])
        i+=1
for number in numbers:
    tempb = boards
    for x, board in enumerate(boards):
        for y, line in enumerate(board):
            for z, num in enumerate(line):
                if num == number:
                    tempb[x][y][z] = f'{num}Y'
        if check_hor_board(tempb[x]) or check_ver_board(tempb[x]):
            print(f'Winner! Board number {x}')
            for line in tempb[x]:
                for num in line:
                    if num[-1] != 'Y':
                        winsum = winsum + int(num)
            print(int(number) * winsum)
            quit()
    boards = tempb

