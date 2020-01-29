# day 20

import math as m

inp = 34000000

# from https://www.programiz.com/python-programming/examples/factor-number 
# with edits from https://www.geeksforgeeks.org/sum-factors-number/
def factors(x): # n -> [list of any factors of n, including 1 and itself]
  l = []
  for i in range(1, int((x+2)/2)):
    if x % i == 0:
      l.append(i)
  l.append(x)
  return l

def presents(n,PartTwo=False): # n -> n, how many presents house n gets
  return sum(factors(n))*(10+1*PartTwo) 

def combi(x,n): #basically just for combining factors and presents
  return sum(d for d in factors(x) if n / d <= 50)

for i in range(10): # trying to find the house that gets more presents than input 
  p = presents(i)
  if p >= inp:
    print(i,p)
    break # hope i used break right because this is going to be a long run
  print(i,p)

# 786240 831600