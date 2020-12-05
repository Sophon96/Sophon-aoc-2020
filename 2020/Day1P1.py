#!/usr/bin/python3

inp = open('../input/aoc-1.in', 'r').readlines()
inp = [int(thing) for thing in inp]

for i in range(len(inp)):
	for i2 in inp[i::]:
		if inp[i] + i2 == 2020:
			print(inp[i] * i2)
			exit(0)
