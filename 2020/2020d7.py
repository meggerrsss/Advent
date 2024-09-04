example = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
lex = example.split('\n')

import pprint 

f = open('2020/inputs/2020d7input.txt', 'r')
inp = f.read()
f.close() 
linp = inp.split('\n')[:-1]

def stringtoset(st):
  lis = st.replace(",","").replace(".","").replace("bags","bag").replace("contain",":").split(" ")
  colour = lis.pop(0) + " " + lis.pop(0)
  next = lis[2:]
  numcoloursin = int(len(next)/4)
  d = {}
  d[colour] = [0]*numcoloursin
  for i in range(numcoloursin):
    itersave = (next[4*i+0],next[4*i+1]+" "+next[4*i+2])  #defines order in dict of list of tuples /cry
    d[colour][i] = itersave
  return d


def flattendict(di):
  return {k: v for d in di for k, v in d.items()}


def allcolours(lod): #list of dicts as in output of flattendict(stringtoset(thing))
  return lod.keys()


def flip(contains):
  contained = {}
  for key in contains:
    for value in contains[key]:
      if value[1] in contained:
        contained[value[1]].append((key,value[0]))
      else:
        contained[value[1]] = [(key,value[0])]
  return contained 


def unpeelonce(containeddict,mycol): # needs an output processed by flip 
  try: firstlayer = containeddict[mycol]
  except: firstlayer = "is outest layer"
  return firstlayer

#this is so broken lol
def iterateunpeel(containeddict,mycol):
  listofouter = []
  todo = [mycol]
  while len(todo)>0:
    if type(todo[0]) == type([0]):
      col = todo[0].pop()
    elif todo[0] == "":
      todo = todo[1:]
      col = todo.pop()
    else: col = todo.pop()
    if unpeelonce(containeddict,col) == "is outest layer":
      return listofouter
    print("colour",col)
    listofouter.append(unpeelonce(containeddict,mycol))
    print("collected list",listofouter)
    x = [unpeelonce(containeddict,col)[t][0] for t in range(len(unpeelonce(containeddict,col)))]
    print("x",x)
    todo.append(x)
    print("todo",todo)
    print("next\n")
  return listofouter


# print processing
mybag = "shiny gold"
workingwith = "example"
if workingwith == "example": a = lex
elif workingwith == "full": a = linp
b = [stringtoset(i) for i in a]
containes = flattendict(b) 
contained = flip(containes)
final = unpeelonce(contained,mybag)

print(final)