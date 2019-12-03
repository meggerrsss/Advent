#advent 2019 day 2 
#input formatting
inp = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0"

import math 

def form(st): # changing string list to list of int
    linp = str.split(st,",")
    for i in range(0, len(linp)): 
        linp[i] = int(linp[i]) 
    return(linp)

linp = form(inp)
backup = linp

def thing(li): # doing the list instructions, outputs list
    ncodes = math.ceil(len(li)/4)
    for i in range(ncodes):
        #print(i)
        instructpos = 4*i
        #print(instructpos)
        #print(li[instructpos])
        if li[instructpos] == 99:
            break
        elif li[instructpos] == 1:
            #print("add")
            li[li[instructpos+3]] = li[li[instructpos+1]]+li[li[instructpos+2]]
        elif li[instructpos] == 2:
            #print("multiply")
            li[li[instructpos+3]] = li[li[instructpos+1]]*li[li[instructpos+2]]
        else: 
            return "no correct instruction"
    return li
    
#print(thing(linp))


#p1 tests
t1 = "1,9,10,3,2,3,11,0,99,30,40,50"
assert(thing(form(t1))==form("3500,9,10,70,2,3,11,0,99,30,40,50"))
t2 = "1,0,0,0,99" #2,0,0,0,99
assert(thing(form(t2))==form("2,0,0,0,99"))
t3 = "2,3,0,3,99" #2,3,0,6,99
assert(thing(form(t3))==form("2,3,0,6,99"))
t4 = "2,4,4,5,99,0" #2,4,4,5,99,9801
assert(thing(form(t4))==form("2,4,4,5,99,9801"))
t5 = "1,1,1,4,99,5,6,0,99" #30,1,1,4,2,5,6,0,99
assert(thing(form(t5))==form("30,1,1,4,2,5,6,0,99"))


#apparently part 2 wants the output to be list[0], after giving explicit tests in part 1 for the output to be a list, so, here's a function
def stupid(lis): #outputs first thing in list
    return lis[0]


def adjust(lis,a,b):    # a is "noun" and b is "verb" despite the fact that the instruction should be the verb
    return [lis[0]]+[a]+[b]+lis[3:]


def findoutput(lis,out):
    noun = 0
    verb = 0 
    for n in range(0,100):
        for v in range(0,100):
            #print(lis)
            new = adjust(lis,n,v)
            #print(new)
            #print(thing(new))
            maybe = stupid(thing(new))
            print("{0},{1},{2}".format(n,v,maybe))
            if maybe == out:
                noun = n 
                verb = v
                break
    return 100*noun+verb      
    

#confirming answer to #1
#assert(stupid(thing(adjust(linp,12,2)))==3101844)

print(findoutput(backup,19690720))

    

    
#p1 show your work
#print(linp)
#a1 = adjust(linp,12,2)
#linp[1]=12
#linp[2]=2
#print(linp)
#print(a1==linp)
#print(thing(linp))