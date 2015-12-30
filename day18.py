__author__ = 'Meghan'

import matplotlib.pyplot as plt
import numpy as np

f = open('day18.txt', 'r')
inp = f.read()
f.close()


def blankgrid(n,m): # n is number of rows, m is number of columns, from day 6
    grid = [[0 for j in xrange(m)] for i in xrange(n)]
    return grid


def initgrid(s, n,m):
    grid = blankgrid(n,m)
    l = s.split('\n')
    for i in range(n):
        grid[i] = list(l[i])
    return grid


def numgrid(grid):
    size = (len(grid), len(grid[0]))
    new = blankgrid(size[0],size[1])
    for i in range(size[0]):
        for j in range(size[1]):
            if grid[i][j] == '#':
                new[i][j] = 1
            else:
                new[i][j] = 0
    return new


def count(mat): # from day 6
    size = (len(mat),len(mat[0])) # i,j
    tally = 0
    for i in range(size[1]):
        for j in range(size[0]):
            if mat[i][j] == "#" or mat[i][j] == "1":
                tally += sum(mat[i])
    return tally


def neighbours(grid,lat,long):
    size = (len(grid),len(grid[0]))
    if lat == 0 and long == 0: #corners
        l = [grid[lat+1][long], grid[lat+1][long+1], grid[lat][long+1]]
    elif lat == 0 and long == size[1]-1:
        l = [grid[lat+1][long], grid[lat+1][long-1], grid[lat][long-1]]
    elif lat == size[0]-1 and long == size[1]-1:
        l = [grid[lat-1][long], grid[lat-1][long-1], grid[lat][long-1]]
    elif lat == size[0]-1 and long == 0:
        l = [grid[lat-1][long], grid[lat-1][long+1], grid[lat][long+1]]
    elif lat == 0: #edges
        l = [grid[lat+1][long], grid[lat+1][long-1], grid[lat+1][long+1], grid[lat][long-1], grid[lat][long+1]]
    elif lat == size[0]-1:
        l = [grid[lat-1][long], grid[lat-1][long-1], grid[lat-1][long+1], grid[lat][long-1], grid[lat][long+1]]
    elif long == 0:
        l = [grid[lat][long+1], grid[lat-1][long+1], grid[lat+1][long+1], grid[lat-1][long], grid[lat+1][long]]
    elif long == size[1]-1:
        l = [grid[lat][long-1], grid[lat-1][long-1], grid[lat+1][long-1], grid[lat-1][long], grid[lat+1][long]]
    else: #centre
        l = [grid[lat+1][long+1], grid[lat][long+1], grid[lat+1][long], grid[lat-1][long+1], grid[lat+1][long-1], grid[lat-1][long], grid[lat-1][long], grid[lat-1][long-1]]
    return l


def neighbourson(grid, lat, long):
    count = 0
    l = neighbours(grid, lat, long)
    for i in l:
        if i == "#" or i == "1":
            count +=1
    return l, count





def switch(grid):
    new = grid
    size = (len(grid),len(grid[0]))
    for i in range(size[0]):
        for j in range(size[1]):
            surround = neighbourson(grid,i,j)[1]
            if grid[i][j] ==1 and (surround == 2 or surround == 3):
                new[i][j] = 1
            elif grid[i][j] ==0 and surround == 3:
                new[i][j] = 1
            else:
                new[i][j] = 0
    return new



def iterswitch(grid,n):
    while n>0:
        new = switch(grid)
        n -=1
        grid = new
    return grid


grid = numgrid(initgrid(inp,100,100))
print neighbourson(grid,10,10)[1]
print iterswitch(grid,1)

#print "Day 18: \nPart 1: {0} \nPart 2: {1}".format("1","2")


grid = np.array(numgrid(initgrid(inp,100,100)))
x = range(100)
y = range(100)
x, y = np.meshgrid(x, y)
plt.pcolormesh(x, y, grid)
plt.colorbar()
plt.show()
