valid = 0
with open('aoc-2.in', 'r') as fin:
	for i in fin:
		split = i.split()
		bounds = tuple(map(int, split[0].split('-')))
		passwd = split[2]
		letter = split[1].strip(":")
		# DEBUG
		# print(split, bounds, passwd, letter)
		if bounds[1] >= passwd.count(letter) >= bounds[0]:
			valid += 1
print(valid)
