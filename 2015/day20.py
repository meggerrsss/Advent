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

#from https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def isprime(n): # n -> whether or not n is prime
  if n<=1:
    return False
  if n<=3:
    return True
  if (n % 2 == 0 or n % 3 == 0):
    return False
  i = 5
  while(i * i <= n):
    if (n % i == 0 or n % (i + 2) == 0):
      return False
    i = i + 6
  return True

def primefactors(x): # n -> [list of prime factors of n]
  f = factors(x)
  pf = []
  for i in f:
    if isprime(i):
      pf.append(i)
  return pf

def presents(n,PartTwo=False): # n -> n, how many presents house n gets
  return sum(factors(n))*(10+PartTwo) 

def combi(x,n): #basically just for combining factors and presents
  return sum(d for d in factors(n) if x / d <= 50)

for i in range(10): # trying to find the house that gets more presents than input 
  p = presents(i)
  if p >= inp:
    print(i,p)
    break # hope i used break right because this is going to be a long run
  print(i,p)
#print(presents(int(0.043005*inp))>inp)
#print(0.043005*inp)

def sumprime(x): #this doesn't work and i'm not really convinced the math was ever right, since it's somehow supposed to get different results when multiple numbers have the same prime factorization. needs more prefixes. 
  l = primefactors(x) 
  t = 0
  m = []
  for i in range(len(l)):
    for j in range(i+1):
      t+= l[i]**j
    m.append(t)
  t = 1
  for i in m:
    t=t*i 
  return t+len(l)

#for i in range(10):
#  print(presents(i))
# [10,30,40,70,60,120,80,150,130]


# 786240 831600