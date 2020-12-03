inp = open('../input/aoc-1.in', 'r').readlines()
inp = [int(thing) for thing in inp]

for i in range(len(inp)):
	for i2 in inp[i::]:
		for i3 in inp[i::]:
			if inp[i] + i2 + i3 == 2020:
				print(inp[i] * i2 * i3)
				exit(0)
