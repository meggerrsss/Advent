# day 20

inp = 34000000

#from https://www.programiz.com/python-programming/examples/factor-number
def factors(x): 
  l = []
  for i in range(1, x + 1):
    if x % i == 0:
      l.append(i)
  return l

def presents(n):
  return sum(factors(n))*10

for i in range(100000):
  if presents(i) == inp:
    print(i)
    break


# [10,30,40,70,60,120,80,150,130]