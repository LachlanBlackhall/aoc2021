#!/usr/bin/python3
import re
import pandas as pd
import numpy as np
f = open('input').read().splitlines()
coordpairs = []
maxx = maxy = danger = 0
for line in f:
	coordpairs.append(re.findall('(\d+,\d+)', line))
for coords in coordpairs:
	for coord in coords:
		if int(coord.split(',')[0]) > maxx: maxx = int(coord.split(',')[0])
		if int(coord.split(',')[1]) > maxy: maxy = int(coord.split(',')[1])
print(f'Max x is {maxx} and max y is {maxy}')
df = pd.DataFrame(np.zeros((maxx+1, maxy+1))).astype('int64')
for coords in coordpairs:
	if coords[0].split(',')[0] == coords[1].split(',')[0] or coords[0].split(',')[1] == coords[1].split(',')[1]:
		if int(coords[0].split(',')[0]) < int(coords[1].split(',')[0]):
			for i in range(int(coords[0].split(',')[0]), int(coords[1].split(',')[0])+1):
				df.iat[int(coords[0].split(',')[1]), i]+=1
		elif int(coords[0].split(',')[0]) > int(coords[1].split(',')[0]):
			for i in range(int(coords[1].split(',')[0]), int(coords[0].split(',')[0])+1):
				df.iat[int(coords[0].split(',')[1]), i]+=1
		if int(coords[0].split(',')[1]) < int(coords[1].split(',')[1]):
			for i in range(int(coords[0].split(',')[1]), int(coords[1].split(',')[1])+1):
				df.iat[i, int(coords[0].split(',')[0])]+=1
		elif int(coords[0].split(',')[1]) > int(coords[1].split(',')[1]):	
			for i in range(int(coords[1].split(',')[1]), int(coords[0].split(',')[1])+1):
				df.iat[i, int(coords[0].split(',')[0])]+=1
for x in range(0, maxx+1):
	for y in range(0, maxy+1):
		if df.iat[y, x] >= 2:
			danger+=1
print(f'There are {danger} spots')
	

