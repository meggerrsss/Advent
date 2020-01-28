# 2015 day 19

inp = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"

rules = [line[:-1].split(" ") for line in open('rules.txt')]
#print(rules)

def mutate(st,r):
  #lett = list(st)
  lett = st
  #n = [] #mutetated string
  s = set() #set 
  for i in range(len(lett)):
    for j in range(len(r)):
      #print(r[j][0])
      if r[j][0] == lett[i]:
        n = str(lett[0:i])+str(r[j][2])+str(lett[i+1:])
        s.add(n)
      if r[j][0] == lett[i:i+2]:
        n = str(lett[0:i])+str(r[j][2])+str(lett[i+2:])
        s.add(n)
  return len(s)

print(mutate(inp,rules))





#testrules = [line[:-1].split(" ") for line in open('testrules.txt')]
#print(mutate("HOH",testrules))
