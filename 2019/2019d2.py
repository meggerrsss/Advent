#advent 2019 day 2 
#input formatting
inp = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0"

def form(st):
    linp = str.split(st,",")
    for i in range(0, len(linp)): 
        linp[i] = int(linp[i]) 
    return(linp)

linp = form(inp)


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


#tests
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

print(linp)
linp[1]=12
linp[2]=2
print(linp)
print(thing(linp))