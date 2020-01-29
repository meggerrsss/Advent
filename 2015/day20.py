# day 20

import math as m

inp = 34000000

#from https://www.programiz.com/python-programming/examples/factor-number
def factors(x): 
  l = []
  for i in range(1, int((x+2)/2)):
    if x % i == 0:
      l.append(i)
  l.append(x)
  return l

def presents(n):
  return sum(factors(n))*10

for i in range(10):
  if presents(i) >= inp:
    print(i)
    break

for i in range(10):
  print(presents(i))


#i probably should do this in reverse  
#print(inp/10)


# [10,30,40,70,60,120,80,150,130]