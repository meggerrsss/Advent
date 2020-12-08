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


#print(linp)
ex = [stringtoset(i) for i in lex]
full = [stringtoset(linp[i]) for i in range(len(linp))]
pprint.pprint(ex)

