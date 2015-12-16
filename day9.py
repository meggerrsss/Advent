__author__ = 'Meghan'

import itertools

f = open('day9.txt', 'r')
inp = f.read()
f.close()


def citieslist(s):
    l = s.split('\n')
    listed = []
    for dist in l:
        part = dist.split()
        listed.append(part[0])
        listed.append(part[2])
    finalset = set(listed)
    return list(finalset)


def dist(a, b):
    with open('day9.txt','r') as f:
        for line in f:
            line = line.split()
            if (line[0] == a and line[2]) == b or (line[0] == b and line[2] == a):
                dis = line[4]
    return int(dis)


def best():
    cities = citieslist(inp)
    perms = list(itertools.permutations(cities))
    nper = len(perms)
    dsums = [0]*nper
    for i in range(nper): #iterating over permutation
        dis = 0
        order = perms[i]
        for citynumber in range(len(order)-1): #iterating over cities within permutation
            dis += dist(order[citynumber],order[citynumber+1])
        dsums[i] = dis
    return min(dsums)

print best()



