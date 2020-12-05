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


def listToDict(inp):
	temp = {lst.split(':')[0]: lst.split(':')[1] for lst in inp}
	return temp


def dictChecker(inp):
	hgt = inp['hgt']
	hclvals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
	eclvals = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	vals = 0
	if 2002 < int(inp['byr']) or int(inp['byr']) < 1920:
		vals += 1
	if 2020 < int(inp['iyr']) or int(inp['iyr']) < 2010:
		vals += 1
	if 2030 < int(inp['eyr']) or int(inp['eyr']) < 2020:
		vals += 1
	if hgt[-1] == 'n':
		if int(hgt.strip('in')) < 59 or int(hgt.strip('in')) > 76:
			vals += 1
	if hgt[-1] == 'm':
		if int(hgt.strip('cm')) < 150 or int(hgt.strip('cm')) > 193:
			vals += 1
	if len(inp['hcl']) != 7 or inp['hcl'][0] != '#'\
		or inp['hcl'][1] not in hclvals\
		or inp['hcl'][2] not in hclvals\
		or inp['hcl'][3] not in hclvals\
		or inp['hcl'][4] not in hclvals\
		or inp['hcl'][5] not in hclvals\
		or inp['hcl'][6] not in hclvals:
		vals += 1
	if inp['ecl'] not in eclvals:
		vals += 1
	if len(inp['pid']) != 9:
		vals += 1
	if vals > 0:
		return False
	else:
		return True


count = 0
for i in big:
	clean = inputParser(i)
	if not inputChecker(clean):
		continue
	cleanDict = listToDict(clean)
	print(cleanDict)
	if dictChecker(cleanDict):
		count += 1
	# if inputChecker(clean):
		# count += 1
print(count)
