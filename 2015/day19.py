# 2015 day 19

inp = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"

rules = [line[:-1].split(" ") for line in open('rules.txt')]
#print(rules)


def mutate(st,r,itera=1,s=set()): #it doesn't wipe clean if run twice in the same file 
  #lett = list(st)
  lett = st
  if itera == 0:
    return s
  else:
    for i in range(len(lett)):
      for j in range(len(r)):
        #print(r[j][0])
        if r[j][0] == lett[i]:
          n = str(lett[:i])+str(r[j][2])+str(lett[i+1:])
          s.add(n)
        if r[j][0] == lett[i:i+2]:
          n = str(lett[:i])+str(r[j][2])+str(lett[i+2:])
          s.add(n) 
    return mutate(st,r,itera-1,s)

#print(len(mutate(inp,rules)))
testrules = [line[:-1].split(" ") for line in open('testrules.txt')]
#print(len(mutate("HOH",testrules)))


#based off a little bit of math from solution 1
 # https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju?utm_source=share&utm_medium=web2x
import re
splat = re.findall('[A-Z][^A-Z]*', inp) #splitting by capital letters
r = splat.count('Rn')
a = splat.count("Ar")
y = splat.count("Y")
print(len(splat) - r - a - 2*y - 1)



#print(unmutate("HOH",testrules))
