inp = list(map(list, map(str.strip, open('../input/aoc-3.in', 'r').readlines())))
print(inp)
bottom = len(inp)
width = len(inp[0])
# print(width)
# print(bottom)
count = 0
for i in inp[0::]:
	# print(inp.index(i))
	ind = (inp.index(i) * 3) % width
	print(ind)
	if i[ind] == '#':
		count += 1
print(count)
