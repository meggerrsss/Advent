import matplotlib.pyplot as plt
import numpy 
from matplotlib import animation
import copy
import math

f = open('input.txt', 'r')
inp = f.read()
f.close()

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


def dist(p1,p2):
  return numpy.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def addtodict(dict,ang,grid,lat,long,ref):
  newang = metangles(ang,'r')
  if grid[lat][long] in [1,'#'] and not ref==(lat,long):
    if newang not in dict:
      dict[newang] = (lat,long) #dict of unique points, hopefully the closest
    elif ang in dict and dist((lat,long),ref) < dist(dict[newang],ref):
      dict[newang] = (lat,long)


def metangles(ang,mod='r'): #the angles of meteorologists 
  if mod == 'd':
    return (90-ang) % 360
  elif mod == 'r':
    return numpy.radians((90-numpy.degrees(ang))%360)


def slopes(grid,ref): #where grid is np array of lists, ref is tuple of (x,y) where x is -row and y is +col coords 
  size = grid.shape
  q1,q2,q3,q4,d,e = {},{},{},{},{},{}
  s = set()
  if grid[ref[0]][ref[1]] in [0,'.']: print("can't put an asteroid here")
  for lat in range(size[0]):
    for long in range(size[1]):
      dx,dy = long-ref[1],lat-ref[0]
      if dx == 0 and dy == 0:
        continue 
      elif dx == 0 and dy<0: 
        ang = -numpy.pi/2
        deg = numpy.degrees(ang)
        addtodict(q1,ang,grid,lat,long,ref)
      elif dx>0 and dy<0: # top right of ref
        ang = numpy.arctan(dy/dx)
        deg = numpy.degrees(ang)
        addtodict(q1,ang,grid,lat,long,ref)
      elif dx>0 and dy == 0:
        ang = -0.00000000000001
        deg = numpy.degrees(ang)
        addtodict(q2,ang,grid,lat,long,ref)
      elif dy>0 and dx>0: # bottom right of ref
        ang = numpy.arctan(dy/dx)
        deg = numpy.degrees(ang)
        addtodict(q2,ang,grid,lat,long,ref)
      elif dx == 0 and dy>0:
        ang = numpy.pi/2
        deg = numpy.degrees(ang)
        addtodict(q3,ang,grid,lat,long,ref)      
      elif dy>0 and dx<0: # bottom left of ref
        ang = numpy.arctan(dy/dx)
        deg = numpy.degrees(ang)
        addtodict(q3,ang,grid,lat,long,ref)   
      elif dy == 0 and dx<0:
        ang = 0.00000000000001
        deg = numpy.degrees(ang)
        addtodict(q4,ang,grid,lat,long,ref)   
      elif dy<0 and dx<0: # top left of ref
        ang = numpy.arctan(dy/dx)
        deg = numpy.degrees(ang)
        addtodict(q4,ang,grid,lat,long,ref)   
      else:
        ang = numpy.arctan(dy/dx)
      e[(lat,long)] = ang #actual list of all points
  total = len(q1)+len(q2)+len(q3)+len(q4)
  return (q1,q2,q3,q4),e,total


def seenperast(grid):
  per = copy.deepcopy(grid)
  size = grid.shape
  for lat in range(size[0]):
    for long in range(size[1]):
      if grid[lat][long] in [1,'#']:
        per[lat][long] = slopes(grid,(lat,long))[-1]
  m = numpy.amax(per)
  for lat in range(size[0]):
    for long in range(size[1]):
      if per[lat][long] == m:
        p = (lat,long)
  return per,m,p


# test cases
with open("t0.txt","r") as f: t0 = numgrid(initgrid(f.read()))
with open("t1.txt","r") as f: t1 = numgrid(initgrid(f.read()))
with open("t2.txt","r") as f: t2 = numgrid(initgrid(f.read()))
with open("t3.txt","r") as f: t3 = numgrid(initgrid(f.read()))
with open("t4.txt","r") as f: t4 = numgrid(initgrid(f.read()))


chart = numgrid(initgrid(inp))
which = t0
print(which)
g = seenperast(which)
print(g[0])
print("max = ",g[1],"at",g[2])


print(metangles(numpy.pi/2,'r'))








