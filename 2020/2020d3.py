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

def pathe(matr,mx,my,star=[0,0]):   #mx>0 for right, my>0 for down
  v = list(matr[star[0]][star[1]])  #still need to generalize 
  pos = star
  lenx = len(matr[0])
  leny = len(matr)
  for j in range(math.ceil(leny/my)):
    pos = [(pos[0]+mx) % lenx,(pos[1]+my) % leny]
    v.append(matr[pos[1]][pos[0]])
  return sum(convert(v))

#part one answer
print(pathe(linp,3,1))

#part two
testslopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
def trymany(matr,tes):
  s = 1
  for x in range(len(tes)):
    v = pathe(matr,tes[x][0],tes[x][1])
    s = s*v
  return s

#part two answer
print(trymany(linp,testslopes))