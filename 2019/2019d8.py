# skipping day 7 because i don't hate myself as much today

import numpy
numbs = [int(i) for i in open('input.txt', 'r').read().strip()]
#print(numbs)

wide = 25
tall = 6
nlayers = len(numbs)/(wide*tall) #100
print(wide,tall,nlayers)
matrix = numpy.reshape(numbs,(int(nlayers),tall,wide))
# god i hope those dimensions are right, previewing at this scale is hard.
# wait i have a small one to test on lol
#print(matrix)

def mat(ar,w,t):
  wide = w
  tall = t
  nlayers = int(len(ar)/(wide*tall))
  matrix = numpy.reshape(numbs,(nlayers,tall,wide))
  return matrix







t0 = "123456789012"
wide0 = 3 
tall0 = 2 
nlayers0 = 2 

#def matrix(s,width,height):
#    nlayers - len(s)/(wide*tall)
    