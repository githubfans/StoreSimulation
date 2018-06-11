import sys
import random


def genword(minchars=3,maxchars=5,istitle=0):
	vocal=('a','e','i','o','u')
	conso=('w','r','t','y','i','p','s','d','f','g','h','j','k','l','z','c','b','n','m')
	group = []
	numchar = random.randint(minchars,maxchars)
	for i in range(numchar):
		rnd = random.randint(0,1)
		if rnd is 0:
			full_name=random.choice(vocal)+random.choice(conso)
		if rnd is 1:
			full_name=random.choice(conso)+random.choice(vocal)
		group.append(full_name)
	#assuming he wants at least some kind of seperator between the names.
	group_string = "".join(group)
	if istitle is 1:
		return group_string.title()
	else:
		return group_string


def genname(minwords=2,maxwords=3,minchars=3,maxchars=5,istitle=1):
	import random
	numword = random.randint(minwords,maxwords)
	group = []
	for i in range(numword):
		dword = genword(minchars,maxchars,istitle)
		group.append(dword)
	return " ".join(group)


def gendesc(minitem=3, maxitem=100, minwords=5, maxwords=10, minchars=3, maxchars=7, istitle=0):
	import random
	numitem = random.randint(minitem,maxitem)
	group = []
	for i in range(numitem):
		ditem = genname(minwords,maxwords,minchars,maxchars, istitle)
		group.append(ditem)
	return ". ".join(group)+"."
