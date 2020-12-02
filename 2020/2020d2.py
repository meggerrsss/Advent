f = open('2020/inputs/2020d2input.txt', 'r')
inp = f.read()
f.close() 

linp = inp.split('\n')

def valid(passex): #a single test
  s = passex.split(' ') #just splitted the sections
  rang = [int(x) for x in s[0].split("-")]   #proud of this
  req = s[1][0]    
  passe = s[2]
  t = passe.count(req)
  return t in range(rang[0],rang[1]+1)

print(valid(linp[0]))

#tests:
a = '1-3 a: abcde'
print(valid(a))
b = '1-3 b: cdefg'
print(valid(b))
c = '2-9 c: ccccccccc'
print(valid(c))

#how many are valid
print(sum([valid(t) for t in linp]))