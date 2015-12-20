__author__ = 'Meghan'

import itertools
import numpy

f = open('day13.txt', 'r')
inp = f.read()
f.close()

f = open('testday13.txt', 'r')
test = f.read()
f.close()


def attendeelist(s): #taken from day9
    l = s.split('\n')
    listed = []
    for comb in l:
        comb = comb.rstrip('.')
        part = comb.split()
        listed.append(part[0])
        listed.append(part[10])
    finalset = set(listed)
    return list(finalset)


def hapamounts(a, b): #taken from day9
    hap = []
    with open('day13.txt','r') as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.rstrip('.')
            line = line.split()
            if (line[0] == a and line[10]) == b or (line[0] == b and line[10] == a):
                if line[2] == 'gain':
                    hap.append(int(line[3]))
                elif line[2] == 'lose':
                    hap.append(-1*int(line[3]))
    return hap


def best(a): #taken from day9
    people = attendeelist(a)
    perms = list(itertools.permutations(people))
    nper = len(perms)
    hsums1 = [0]*nper
    hsums2 = [0]*nper
    for i in range(nper): #iterating over permutation
        order = perms[i]
        haplist = [0]*len(order)
        for person in range(len(order)-1): #iterating over people within permutation
            inter = sum(hapamounts(order[person],order[person+1]))
            haplist[person] = inter
        haplist[len(order)-1] = sum(hapamounts(order[len(order)-1],order[0])) #could use mod but i want to make sure it works first
        worstpair = min(haplist)
        hsums1[i] = sum(haplist)
        hsums2[i] = sum(haplist)-worstpair
    return (max(hsums1),max(hsums2))

out = best(inp)
print "Day 13: \nPart 1: {0} \nPart 2: {1}".format(out[0],out[1])