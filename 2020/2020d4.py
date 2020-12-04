f = open('2020/inputs/2020d4input.txt', 'r')
inp = f.read()
f.close() 
linp = inp.split("\n\n")
print(linp)

def inn(st,key): # is the necessary value IN the string
  st = st.replace(":"," ")
  st = st.replace("\n"," ")
  return key in st.split(" ")

needed = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def countvalues(st,need = needed): # how many necessary values are in the string
  v = [inn(st,k) for k in need]
  return sum(v)

print(countvalues(linp[0]))

counter = 0
for person in linp:
  print(person)
  print(countvalues(person))
  if countvalues(person) == len(needed):
    counter += 1
print(counter)