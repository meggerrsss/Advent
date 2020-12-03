f = open('2020/inputs/2020d3input.txt', 'r')
inp = f.read()
f.close() 

linp = inp.split('\n')

print(linp)

def extend(matr):
  lenx = len(matr[0])
  leny = len(matr)
  while lenx<leny:
    matr = [row+row for row in matr]
    lenx = len(matr[0])
    leny = len(matr)
  return matr

print(extend(linp))