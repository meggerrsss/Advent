__author__ = 'Meghan'

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import copy

f = open('input.txt', 'r')
inp = f.read()
f.close()


def blankgrid(n, m): # n is number of rows, m is number of columns, from day 6
    grid = [[0 for j in range(m)] for i in range(n)]
    return grid


def initgrid(s, n, m):
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
    for i in range(size[0]):
        for j in range(size[1]):
            if mat[i][j] == 1:
                tally += 1
    return tally


def neighbours(grid,lat,long): # given a grid and a position in the grid, returns what state the neighbours are in
    size = (len(grid),len(grid[0]))
    if lat == 0 and long == 0: #corners, top left
        l = [grid[lat+1][long], grid[lat+1][long+1], grid[lat][long+1]]
    elif lat == 0 and long == size[1]-1: #corners, top right?
        l = [grid[lat+1][long], grid[lat+1][long-1], grid[lat][long-1]]
    elif lat == size[0]-1 and long == size[1]-1: #corners, bottom right
        l = [grid[lat-1][long], grid[lat-1][long-1], grid[lat][long-1]]
    elif lat == size[0]-1 and long == 0: #corners, bottom left?
        l = [grid[lat-1][long], grid[lat-1][long+1], grid[lat][long+1]]
    elif lat == 0: #edges, top?
        l = [grid[lat+1][long], grid[lat+1][long-1], grid[lat+1][long+1], grid[lat][long-1], grid[lat][long+1]]
    elif lat == size[0]-1: #edges, bottom?
        l = [grid[lat-1][long], grid[lat-1][long-1], grid[lat-1][long+1], grid[lat][long-1], grid[lat][long+1]]
    elif long == 0: #edges, left? 
        l = [grid[lat][long+1], grid[lat-1][long+1], grid[lat+1][long+1], grid[lat-1][long], grid[lat+1][long]]
    elif long == size[1]-1: #edges, right?
        l = [grid[lat][long-1], grid[lat-1][long-1], grid[lat+1][long-1], grid[lat-1][long], grid[lat+1][long]]
    else: #centre
        l = [grid[lat+1][long+1], grid[lat][long+1], grid[lat+1][long], grid[lat-1][long+1], grid[lat+1][long-1], grid[lat-1][long], grid[lat][long-1], grid[lat-1][long-1]]
    return l


def neighbourson(grid, lat, long):
    count = 0
    l = neighbours(grid, lat, long)
    for i in l:
        if i == "#" or i == 1:
            count +=1
    return l, count


def switch(grid):
  new = copy.deepcopy(grid)
  size = (len(grid),len(grid[0]))
  for i in range(size[0]):
    for j in range(size[1]):
      surround = neighbourson(grid,i,j)[1]
      if grid[i][j] in [1,'#'] and surround in [2,3]:
        new[i][j] = 1
      elif grid[i][j] in [0,'.'] and surround == 3:
        new[i][j] = 1
      else: 
        new[i][j] = 0
  return new



def iterswitch(grid,n):
    time = [grid]
    while n>0:
        new = switch(grid)
        time.append(new)
        grid = new
        n -= 1
    return grid


#grid = numgrid(initgrid(inp,100,100))
#print(neighbourson(grid,10,10)[1])
#print count(iterswitch(grid,100))

#print "Day 18: \nPart 1: {0} \nPart 2: {1}".format("1","2")


#grid = np.array(numgrid(initgrid(inp,100,100)))
#x = range(100)
#y = range(100)
#x, y = np.meshgrid(x, y)
#plt.pcolormesh(x, y, grid)
#plt.colorbar()
#plt.show()


t0 = ".#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####.."
grid0 = initgrid(t0,6,6)
print(numgrid(grid0))
print(neighbourson(grid0,0,2))
print(iterswitch(numgrid(grid0),4))