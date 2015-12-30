__author__ = 'Meghan'

from itertools import combinations

containers = [int(line) for line in open('day17.txt')]


def ways():
    total = 0
    lengths = []
    for i in range(len(containers)):
        for c in combinations(containers, i):
            if sum(c) == 150:
                total += 1
                lengths.append(len(c))
    least = lengths[0]
    leasts = 0
    for i in lengths:
        if i == least:
            leasts +=1
    return total, leasts


print "Day 17: \nPart 1: {0} \nPart 2: {1}".format(ways()[0], ways()[1])
