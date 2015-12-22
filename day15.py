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


def candyscore(matrix, a, b, c, d, r):
    cal = a*matrix[0][5] + b*matrix[1][5] + c*matrix[2][5] + d*matrix[3][5]
    if r == 2 and not cal == 500:
        return 0
    else:
        cap = a*matrix[0][1] + b*matrix[1][1] + c*matrix[2][1] + d*matrix[3][1]
        dur = a*matrix[0][2] + b*matrix[1][2] + c*matrix[2][2] + d*matrix[3][2]
        fla = a*matrix[0][3] + b*matrix[1][3] + c*matrix[2][3] + d*matrix[3][3]
        tex = a*matrix[0][4] + b*matrix[1][4] + c*matrix[2][4] + d*matrix[3][4]
        rawp = cap*dur*fla*tex
        if cap<=0:
            cap = 0
        if dur<=0:
            dur = 0
        if fla<=0:
            fla = 0
        if tex<=0:
            tex = 0
        newp = cap*dur*fla*tex
        return newp


def best(s,r):
    mat = propmatrix(s)
    scores = []
    for a in range(0,100+1):
        for b in range(0,100-a+1):
            for c in range(0,100-a-b+1):
                for d in range(0,100-a-b-c+1):
                    score = candyscore(mat, a, b, c, d, r)
                    if score >0:
                        scores.append(score)
    return scores


print "Day 15: \nPart 1: {0} \nPart 2: {1}".format(max(best(inp,1)), max(best(inp,2)))