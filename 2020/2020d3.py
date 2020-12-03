f = open('2020/inputs/2020d3input.txt', 'r')
inp = f.read()
f.close() 
linp = inp.split('\n')

import math 

def extend(matr,x=1):
  lenx = len(matr[0])
  leny = len(matr)
  while lenx<=leny:
    matr = [row+row for row in matr]
    lenx = len(matr[0])
    leny = len(matr)
    print(matr)
  return matr

#print(extend(linp))

def pathe1(matr,mx,my):
  pos = (0,0)
  leny = len(matr)
  v = [matr[0][0]]
  print(v)
  for j in range(leny-1):
    pos = (pos[0]+mx, pos[1]+my)
    v.append(matr[pos[1]][pos[0]])
  return v 

#inxt = extend(linp)

def convert(vec):
  v = [0] * len(vec)
  for s in range(len(vec)):
    if vec[s] != "." :   #idk how to find hashtags
      v[s] = 1
  return v

def pathe(matr,mx,my,star=[0,0]):
  v = list(matr[0][0])
  pos = star
  lenx = len(matr[0])
  leny = len(matr)
  for j in range(math.ceil(leny/my)):
    pos = [(pos[0]+mx) % lenx,(pos[1]+my) % leny]
    print(pos)
    v.append(matr[pos[1]][pos[0]])
  return v

print(pathe(linp,3,1))

#number of trees hit (tree = #)
print(convert(pathe(linp,3,1)))

