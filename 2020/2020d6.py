f = open('2020/inputs/2020d6input.txt', 'r')
inp = f.read()
f.close() 
linp = inp.split('\n\n')

print(linp)

def toset(li):
  setted = [0] * len(li)
  for x in range(len(li)):
    setted[x] = set(li[x].replace('\n',''))
  return setted

print(toset(linp))

def sumsetlengths(los): # los = list of sets, output from toset
  v = [len(x) for x in los]
  print(v)
  return sum(v)

print(sumsetlengths(toset(linp)))