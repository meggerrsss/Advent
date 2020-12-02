f = open('2020/inputs/2020d1input.txt', 'r')
inp = f.read()
f.close() 

linp = inp.split('\n')
linpt = [int(n) for n in linp]
print(linpt)

def twentytwenty(li):
  for t in range(len(li)):
    if li[t] < 2020:
      for s in range(t,len(li)):
        if li[t]+li[s] == 2020:
          return li[s]*li[t]

# part one answer 
print(twentytwenty(linpt))