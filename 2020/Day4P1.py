#!/usr/bin/python3

import re

big = list()
with open('../input/aoc-4.in', 'r') as fin:
	tmp = list()
	for i in fin:
		if i != '\n':
			tmp.append(i)
		else:
			big.append(tmp)
			tmp = list()
	big.append(tmp)
# print(big)


def inputParser(inp):
	tmp = list()
	for i in inp:
		i2 = i.strip().split()
		tmp.extend(i2)
	return tmp


def inputChecker(inp):
	temp = [0, 0, 0, 0, 0, 0, 0]
	for i in inp:
		# print(i)
		if type(re.search("^byr:", i)) == re.Match:
			temp[0] = 1
		if type(re.search("^iyr:", i)) == re.Match:
			temp[1] = 1
		if type(re.search("^eyr:", i)) == re.Match:
			temp[2] = 1
		if type(re.search("^hgt:", i)) == re.Match:
			temp[3] = 1
		if type(re.search("^hcl:", i)) == re.Match:
			temp[4] = 1
		if type(re.search("^ecl:", i)) == re.Match:
			temp[5] = 1
		if type(re.search("^pid:", i)) == re.Match:
			temp[6] = 1
	if temp.count(0) == 0:
		return True
	else:
		return False


count = 0
for i in big:
	clean = inputParser(i)
	# print(clean)
	if inputChecker(clean):
		count += 1
print(count)
