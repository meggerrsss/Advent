import numpy
numbs = [int(i) for i in open('input.txt', 'r').read().strip()]
wide,tall=25,6

def mat(ar,w,t):
  wide,tall = w,t
  nlayers = int(len(ar)/(wide*tall))
  matrix = numpy.reshape(ar,(nlayers,tall,wide))
  return matrix

t00 = [int(i) for i in "123456789012".strip()]
wide0,tall0 = 3 ,2
mat0 = mat(t00,wide0,tall0)

def count(matr):
  nlayers,tall,wide = len(matr),len(matr[0]),len(matr[0][0])
  d = numpy.zeros((nlayers,4))
  for layer in range(len(matr)):
    d[layer][0] = layer #original layer number
    d[layer][1] = numpy.count_nonzero(matr[layer] == 0)
    d[layer][2] = numpy.count_nonzero(matr[layer] == 1)
    d[layer][3] = numpy.count_nonzero(matr[layer] == 2)
  return d

a = count(mat(numbs,wide,tall))
sorted = a[a[:,1].argsort()] # sort by number of zeroes
row = sorted[0] # row with fewest zeroes
ans = int(row[2])*int(row[3]) # number of 1s in least-zero-line multiplied by number of 2s in least-zero-line


# p2

def flatten(matr):
  nlayers,tall,wide = len(matr),len(matr[0]),len(matr[0][0])
  flat = numpy.zeros((tall,wide)) +2
  for layer in range(nlayers):
    for t in range(tall):
      for w in range(wide):
        if flat[t][w]==2:
          #print("w =",w,"t =",t,"l =",layer,"v =",flat[t][w])
          flat[t][w] = matr[layer][t][w]
  return flat

t1 = [int(i) for i in "0222112222120000".strip()]
wide1,tall1 = 2,2
mat1 = mat(t1,wide1,tall1)
#print(mat1)

print(flatten(mat(numbs,wide,tall)))
#and then i used excel to display it because python wasn't letting me output something wide enough to visually process it