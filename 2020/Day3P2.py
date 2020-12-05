#!/usr/bin/python3

inp = list(map(list, map(str.strip, open('../input/aoc-3.in', 'r').readlines())))

width = len(inp[0])


def tree1(y, x=1):
	count = 0
	for i in inp[0::x]:
		ind = (inp.index(i) * y) % width
		if i[int(ind)] == '#':
			count += 1
	return count


a = tree1(1)
b = tree1(3)
c = tree1(5)
d = tree1(7)
# I used e back when I intended to use tree1() to do everything,
# but that didn't work, so I used f and don't feel like changing it to e
f = tree1(0.5, 2)
total = a * b * c * d * f
print(total)
