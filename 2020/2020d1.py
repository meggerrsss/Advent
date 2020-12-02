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

def twentytwenty3(li):
  for t in range(len(li)):
    if li[t] < 2020:
      for s in range(t,len(li)):
        if li[t]+li[s] < 2020:
          for r in range(s,len(li)):
            if li[t]+li[s]+li[r] == 2020:
              return li[s]*li[t]*li[r]


# part two answer 
print(twentytwenty3(linpt))



# attempting some optimization because gianni's complaining
def twentytwentyagain(li):
  li = set(li)
  for s in li:
    if 2020-s in li:
      return s*(2020-s)

print(twentytwentyagain(linpt))