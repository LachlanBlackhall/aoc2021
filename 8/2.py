#!/usr/bin/python3
from collections import defaultdict


def contains(known, item):
    for char in known:
        if char not in item:
            return False
    return True


def return_false():
    return False


# 2, 3, 4 and 7 have a unique component number
# As such we only need to check them once
def check_uniques(nums, current_line):
    remaining = current_line.copy()
    for item in current_line:
        if len(item) == 2:
            for char in item:
                nums['1'].append(char)
            remaining.remove(item)
        elif len(item) == 4:
            for char in item:
                nums['4'].append(char)
            remaining.remove(item)
        elif len(item) == 3:
            for char in item:
                nums['7'].append(char)
            remaining.remove(item)
        elif len(item) == 7:
            for char in item:
                nums['8'].append(char)
            remaining.remove(item)
    return nums, remaining


# With the uniques identified we can derive the 6 long numbers
def check_sixes(nums, remaining, item):
    if nums['1'][0] not in item or nums['1'][1] not in item:
        for char in item:
            nums['6'].append(char)
        remaining.remove(item)
    if contains(nums['1'], item):
        if contains(nums['4'], item):
            for char in item:
                nums['9'].append(char)
            remaining.remove(item)
        else:
            for char in item:
                nums['0'].append(char)
            remaining.remove(item)
    return nums, remaining


# The fives usually come last in the order so we need to return early
# so that we don't try to remove an element that was removed by
# an earlier check
def check_fives(nums, remaining, item):
    if contains(nums['7'], item):
        for char in item:
            nums['3'].append(char)
        remaining.remove(item)
        if len(remaining) == 1:
            return nums, remaining
    misses = 0
    for part in nums['6']:
        if part not in item:
            misses += 1
    if misses == 1:
        for char in item:
            nums['5'].append(char)
        remaining.remove(item)
        if len(remaining) == 1:
            return nums, remaining
    if len(remaining) == 1:
        for char in item:
            nums['2'].append(char)
        remaining.remove(item)
    return nums, remaining


# With all numbers identifed we can identify the correct translations
# with simple checks, to truly understand the logic the visual aid is
# helpful
def get_chars(nums):
    chars = defaultdict(return_false)
    for char in nums['1']:
        if char in nums['2']:
            chars[char] = 'c'
        else:
            chars[char] = 'f'
    for char in nums['7']:
        if char not in nums['1']:
            chars[char] = 'a'
    for char in nums['4']:
        if char not in nums['1']:
            if char in nums['0']:
                chars[char] = 'b'
            else:
                chars[char] = 'd'
    for char in nums['0']:
        if not chars[char]:
            if char not in nums['3']:
                chars[char] = 'e'
            else:
                chars[char] = 'g'
    return chars


f = open('input').read().splitlines()
split_list = []
final_count = 0
screens = {'abcefg': 0, 'cf': 1, 'acdeg': 2,
           'acdfg': 3, 'bcdf': 4, 'abdfg': 5,
           'abdefg': 6, 'acf': 7, 'abcdefg': 8,
           'abcdfg': 9}

# Get each line from the file and split it
# into input and output based on the |
for line in f:
    split_list.append([line.split('|')[0].split(' '),
                       line.split('|')[1].split(' ')])

for line in split_list:
    line[0] = [x for x in line[0] if x]  # Strip empty item from list
    line[1] = [x for x in line[1] if x]
    lineresult = ''
    nums = {'0': [], '1': [], '2': [], '3': [],
            '4': [], '5': [], '6': [], '7': [],
            '8': [], '9': []}
    nums, remaining = check_uniques(nums, line[0])
    while len(remaining) != 0:
        for item in line[0]:
            if len(item) == 6:
                nums, remaining = check_sixes(nums, remaining, item)
            if len(item) == 5 and nums['6']:
                nums, remaining = check_fives(nums, remaining, item)
        line[0] = remaining
    chars = get_chars(nums)
    # With all chars translated we can convert the output to numbers
    for item in line[1]:
        output = ''
        for char in item:
            output += chars[char]
        lineresult += str(screens[''.join(sorted(output))])
    final_count += int(lineresult)
print(final_count)
