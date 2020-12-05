#!/usr/bin/python3

valid = 0
with open('../input/aoc-2.in', 'r') as fin:
	for i in fin:
		split = i.split()
		bounds = tuple(map(int, split[0].split('-')))
		passwd = split[2]
		letter = split[1].strip(":")
		# DEBUG
		# print(split, bounds, passwd, letter)
		# Finally got to use that stupid ^ XOR symbol
		if (passwd[bounds[0] - 1] == letter) ^ (passwd[bounds[1] - 1] == letter):
			valid += 1
print(valid)
