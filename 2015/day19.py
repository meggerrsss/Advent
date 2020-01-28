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

print(len(mutate(inp,rules)))
testrules = [line[:-1].split(" ") for line in open('testrules.txt')]
print(len(mutate("HOH",testrules)))

#iterate?





#reverse?
startt = "e"

def unmutate(st,r):
  lett = st
  s = set()


#print(unmutate("HOH",testrules))






