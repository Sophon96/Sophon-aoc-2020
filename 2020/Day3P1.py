#!/usr/bin/python3

inp = list(map(list, map(str.strip, open('../input/aoc-3.in', 'r').readlines())))

width = len(inp[0])
count = 0

for i in inp[0::]:
	ind = (inp.index(i) * 3) % width
	if i[ind] == '#':
		count += 1

print(count)
