f = open('2020/inputs/2020d3input.txt', 'r')
inp = f.read()
f.close() 
linp = inp.split('\n')


def extend(matr,x=1):
  lenx = len(matr[0])
  leny = len(matr)
  while lenx<=leny:
    matr = [row+row for row in matr]
    lenx = len(matr[0])
    leny = len(matr)
    print(matr)
  return matr

print(extend(linp))

def pathe(matr,mx,my):
  pos = (0,0)
  leny = len(matr)
  v = [matr[0][0]]
  print(v)
  for j in range(leny-1):
    pos = (pos[0]+mx, pos[1]+my)
    v.append(matr[pos[1]][pos[0]])
  return v 

inxt = extend(linp)
print(pathe(inxt,3,1)))
