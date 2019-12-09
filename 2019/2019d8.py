import numpy
numbs = [int(i) for i in open('input.txt', 'r').read().strip()]
wide,tall=25,6

# god i hope those dimensions are right, previewing at this scale is hard.
# wait i have a small one to test on lol

def mat(ar,w,t):
  wide = w
  tall = t
  nlayers = int(len(ar)/(wide*tall))
  matrix = numpy.reshape(ar,(nlayers,tall,wide))
  return matrix

#print(mat(numbs,wide,tall)[0][0])

t00 = [int(i) for i in "123456789012".strip()]
wide0,tall0 = 3 ,2
mat0 = mat(t00,wide0,tall0)
#print(mat0)

def count(matr):
  nlayers,tall,wide = len(matr),len(matr[0]),len(matr[0][0])
  d = numpy.zeros((nlayers,3))
  print(nlayers,tall,wide)
  for layer in range(len(matr)):
    d[layer][0] = numpy.count_nonzero(matr[layer] == 0)
    d[layer][1] = numpy.count_nonzero(matr[layer] == 1)
    d[layer][2] = numpy.count_nonzero(matr[layer] == 2)
  return d
#print(numpy.zeros((100,3)))


print(count(mat0))
#def matrix(s,width,height):
#    nlayers - len(s)/(wide*tall)
