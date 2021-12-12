#!/usr/bin/python3
import time, pdb, traceback


def get_matching(char, open_brackets, close_brackets):
    for x, bracket in enumerate(open_brackets):
        if char == bracket:
            return close_brackets[x]


f = open('test').read().splitlines()
# f = open('input').read().splitlines()
split_list = []
open_brackets = ['(', '[', '{', '<']
close_brackets = [')', ']', '}', '>']
score = 0
scores = []

for line in f:
    split_list.append(line)

for line in split_list:
    errored = False
    legal_close = []
    print('New line')
    i = 0
    while i < len(line):
        char = line[i]
        print(f'Up to {char}')
        if char in open_brackets:
            legal_close.append(get_matching(char, open_brackets, close_brackets))
            print(f'Found another opener {char}, legal closes are now {legal_close}')
        elif not errored and len(legal_close) != 0:
            print(f' Checking {char} and {legal_close[-1]}')
            if char != legal_close.pop():
                for v, bracket in enumerate(close_brackets):
                    if char == bracket:
                        if v == 0:
                            print(f'Expected {legal_close[-1]} and found {char}')
                            score += 3
                        elif v == 1:
                            print(f'Expected {legal_close[-1]} and found {char}')
                            score += 57
                        elif v == 2:
                            print(f'Expected {legal_close[-1]} and found {char}')
                            score += 1197
                        elif v == 3:
                            print(f'Expected {legal_close[-1]} and found {char}')
                            score += 25137
                errored = True
            else:
                print(f'Closed {char}')
        i += 1
        # time.sleep(0.5)
        if errored:
            break

print(score)

