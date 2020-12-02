f = open('2020/inputs/2020d2input.txt', 'r')
inp = f.read()
f.close() 

linp = inp.split('\n')

def valid1(passex): #a single test
  s = passex.split(' ') #just splitted the sections
  rang = [int(x) for x in s[0].split("-")]   #proud of this
  req = s[1][0]    
  passe = s[2]
  t = passe.count(req)
  return t in range(rang[0],rang[1]+1)

#print(valid1(linp[0]))

#how many are valid
print(sum([valid1(t) for t in linp]))



def valid2(passex): 
  s = passex.split(' ') 
  poses = [int(x) for x in s[0].split("-")]  
  req = s[1][0]    
  passe = s[2]
  first = passe[poses[0]-1] == req
  second = passe[poses[1]-1] == req
  return first+second == 1

print(valid2(linp[0]))

#how many are valid
print(sum([valid2(t) for t in linp]))


#tests:
a = '1-3 a: abcde'
print(valid2(a))
b = '1-3 b: cdefg'
print(valid2(b))
c = '2-9 c: ccccccccc'
print(valid2(c))