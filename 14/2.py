#!/usr/bin/python3

# f = open('test').read().splitlines()
f = open('input').read().splitlines()
insertions = []
template = f[0]
unique_chars = set(template)
pair_counts = {}
char_counts = {}

for i in range(2,len(f)):
    unique_chars.add(f[i].split(' ')[2])
    insertions.append([f[i].split(' ')[0], f[i].split(' ')[2]])

for x in unique_chars:
    char_counts[x] = 0

for x in template:
    char_counts[x] += 1

for i in unique_chars:
    for x in unique_chars:
        pair_counts[i+x] = 0

for i, char in enumerate(template):
    if i != len(template)-1:
        pair_counts[char+template[i+1]] += 1

copy_pairs = pair_counts.copy()
copy_chars = char_counts.copy()
for i in range(0, 40):
    for insertion in insertions:
        if pair_counts[insertion[0]] > 0:
            split_pair = list(insertion[0])
            copy_pairs[insertion[0]] -= pair_counts[insertion[0]]
            copy_pairs[split_pair[0] + insertion[1]] += pair_counts[insertion[0]]
            copy_pairs[insertion[1] + split_pair[1]] += pair_counts[insertion[0]]
            copy_chars[insertion[1]] += pair_counts[insertion[0]]
    pair_counts = copy_pairs.copy()
    char_counts = copy_chars.copy()

counter = []
for char in char_counts:
    counter.append(char_counts[char])

print(max(counter) - min(counter))

