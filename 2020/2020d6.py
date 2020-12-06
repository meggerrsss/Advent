f = open('2020/inputs/2020d6input.txt', 'r')
inp = f.read()
f.close() 
linp = inp.split('\n\n')


def tosetpart1(li):
  setted = [0] * len(li)
  for x in range(len(li)):
    setted[x] = set(li[x].replace('\n',''))
  return setted


def tosetpart2(li):
  setted = [0] * len(li)
  for x in range(len(li)):
    splitfirst = li[x].split('\n')
    splitfirst = [set(t) for t in splitfirst]
    setted[x] = set(splitfirst[0])
    for y in splitfirst:
      setted[x] = setted[x].intersection(y)
    numpeep = li[x].count('\n')+1
  return setted


print(tosetpart2(linp))

def sumsetlengths(los): # los = list of sets, output from toset
  v = [len(x) for x in los]
  return sum(v)

print(sumsetlengths(tosetpart2(linp)))