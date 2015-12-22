__author__ = 'Meghan'

f = open('day15.txt', 'r')
inp = f.read()
f.close()


def interpret(s):
    l = s.split()
    for i in range(len(l)):
        l[i] = l[i].rstrip(',')
        l[i] = l[i].rstrip(':')
    ing = l[0]
    capacity = int(l[2])
    durability = int(l[4])
    flavour = int(l[6])
    texture = int(l[8])
    calories = int(l[10])
    return (ing, capacity, durability, flavour, texture, calories)


def blankgrid(n,m): # n is number of rows, m is number of columns, taken from day 6
    grid = [[0 for j in xrange(m)] for i in xrange(n)]
    return grid


def propmatrix(s): #i is each ingredient, j is position of its properties
    l = s.split('\n')
    grid = blankgrid(4,6)
    for i in range(len(l)):
        grid[i] = interpret(l[i])
    return grid


print propmatrix(inp)


#print "Day 15: \nPart 1: {0} \nPart 2: {1}".format(a,b)