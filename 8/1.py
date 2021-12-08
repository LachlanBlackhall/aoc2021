#!/usr/bin/python3
f = open('test').read().splitlines()
split_list = []
final_count = 0
for line in f:
    split_list.append([line.split('|')[0].split(' '), line.split('|')[1].split(' ')])
print(split_list)
for line in split_list:
    for output_item in line[1]:
        if len(output_item) == 2:
            print(output_item)
            final_count+=1
        if len(output_item) == 4:
            print(output_item)
            final_count+=1
        if len(output_item) == 3:
            print(output_item)
            final_count+=1
        if len(output_item) == 7:
            print(output_item)
            final_count+=1
print(final_count)

