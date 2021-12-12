#!/usr/bin/python3
import time, pdb, traceback, statistics


def get_matching(char, open_brackets, close_brackets):
    for x, bracket in enumerate(open_brackets):
        if char == bracket:
            return close_brackets[x]


# f = open('test').read().splitlines()
f = open('input').read().splitlines()
split_list = []
open_brackets = ['(', '[', '{', '<']
close_brackets = [')', ']', '}', '>']
scores = []

for line in f:
    split_list.append(line)

for line in split_list:
    errored = False
    legal_close = []
    score = 0
    for char in line:
        print(f'Up to {char}')
        if char in open_brackets:
            legal_close.append(get_matching(char, open_brackets, close_brackets))
            print(f'Found another opener {char}, legal closes are now {legal_close}')
        elif char != legal_close.pop():
            errored = True
            break      
    if len(legal_close) != 0 and not errored:
        legal_close.reverse()
        for close in legal_close:
            if close == ')':
                score = score * 5 + 1
            if close == ']':
                score = score * 5 + 2
            if close == '}':
                score = score * 5 + 3
            if close == '>':
                score = score * 5 + 4
        scores.append(score)
        print(f'{legal_close} had score of {score}')

print(scores)
print(sorted(scores))
print(sorted(scores)[len(scores)//2])

