__author__ = 'Meghan'

import numpy as np

# http://adventofcode.com/day/3

f = open('day3.txt', 'r')
inp = f.read()
f.close()


def matout(s):
    l = list(s)
    presents = len(l)
    houses = np.zeros((presents+1, 3))
    lat = 0
    long = 0
    for i in range(presents):
        if l[i] == '^':
            lat += 1
        elif l[i] == 'v':
            lat -= 1
        elif l[i] == '>':
            long += 1
        elif l[i] == '<':
            long -= 1
        houses[i+1] = np.array([lat, long, 0])
    return houses # nx3 matrix with lat, long, and pres.


def houselist(s):
    l = list(s)
    presents = len(l)
    houses = ['0 0']
    lat = 0
    long = 0
    for i in range(presents):
        if l[i] == '^':
            lat += 1
        elif l[i] == 'v':
            lat -= 1
        elif l[i] == '>':
            long += 1
        elif l[i] == '<':
            long -= 1
        temp = str(lat)+' '+str(long)
        houses.append(temp)
    return set(houses)


def odds(s):
    li = []
    for i in range(len(s)):
        if i%2 == 0:
            li.append(s[i])
    return ''.join(li)


def evens(s):
    li = []
    for i in range(len(s)):
        if i%2 == 1:
            li.append(s[i])
    return ''.join(li)


def duo(s):
    santa = odds(s)
    robo = evens(s)
    santaset = houselist(santa)
    roboset = houselist(robo)
    fullset = santaset|roboset
    return fullset

print "Day 3: \nPart 1: {0} \nPart 2: {1}".format(len(houselist(inp)), len(duo(inp)))


# test cases
def test_answer():
    t1 = ">"
    t2 = "^>v<"
    t3 = "^v^v^v^v^v"
    t4 = "^v"
    assert len(houselist(t1)) == 2
    assert len(houselist(t2)) == 4
    assert len(houselist(t3)) == 2
    assert len(duo(t4)) == 3
    assert len(duo(t2)) == 3
    assert len(duo(t3)) == 11

test_answer()
