inp = open('aoc-1.in', 'r').readlines()
inp = [int(thing) for thing in inp]
print(inp)
# sum1 = int()
# sum2 = int()
for i in range(len(inp)):
	for i2 in inp[i::]:
		for i3 in inp[i::]:
			if inp[i] + i2 + i3 == 2020:
				print(inp[i] * i2 * i3)
				# print(inp[i], i2, i3)
				exit(0)
