import numpy 
import math

f = open('input.txt', 'r')
inp = f.read()
f.close()
print(inp)

# from 2015 day 18
def blankgrid(n, m): # n is number of rows, m is number of columns, from day 6
    grid = [[0 for j in range(m)] for i in range(n)]
    return grid

# from 2015 day 18, removed n,m inputs and changed output to numpy.array
def initgrid(s):
    l = s.split('\n')
    size = (len(l),len(l[0]))
    grid = blankgrid(size[0],size[1])
    for i in range(size[0]):
        grid[i] = list(l[i])
    return numpy.array(grid)

# from 2015 day 18, 1 is the position of each asteroid 
def numgrid(grid):
    size = (len(grid), len(grid[0]))
    new = blankgrid(size[0],size[1])
    for i in range(size[0]):
        for j in range(size[1]):
            if grid[i][j] == '#':
                new[i][j] = 1
            else:
                new[i][j] = 0
    return numpy.array(new)


def slopes(grid,ref): #where grid is np array of lists, ref is tuple of (x,y) coords 
  size = grid.shape
  d = {}
  for lat in size[0]:
    for long in size[1]:
      dx,dy = long-ref[0],lat-ref[1]
      d[(lat,long)] = math.arctan(dy/dx)


chart = numgrid(initgrid(inp))
print(chart.shape)







with open("t0.txt","r") as f: t0 = numgrid(initgrid(f.read()))
with open("t1.txt","r") as f: t1 = numgrid(initgrid(f.read()))
with open("t2.txt","r") as f: t2 = numgrid(initgrid(f.read()))
with open("t3.txt","r") as f: t3 = numgrid(initgrid(f.read()))
with open("t4.txt","r") as f: t4 = numgrid(initgrid(f.read()))

